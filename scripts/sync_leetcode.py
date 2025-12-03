#!/usr/bin/env python3
"""
Fetch accepted LeetCode submissions and save them to files.

Auth:
- Uses LEETCODE_SESSION cookie (required). Provide via GitHub Secret.
- Script will GET the homepage to obtain csrftoken cookie and then use GraphQL.

Output:
- Writes files to solutions/{language}/{question_id}-{title_slug}.{ext}
- Adds a small header comment with metadata.
- Skips writing files if content is unchanged.

Notes:
- If LEETCODE_SESSION is invalid/expired, the script will log errors. Refresh cookie and update secret.
- Be considerate of rate limits; this script sleeps briefly between detailed fetches.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, Optional

import requests

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")

OUT_DIR = Path("solutions")
OUT_DIR.mkdir(parents=True, exist_ok=True)

LANG_INFO = {
    "python": (".py", "#"),
    "python3": (".py", "#"),
    "cpp": (".cpp", "//"),
    "java": (".java", "//"),
    "javascript": (".js", "//"),
    "typescript": (".ts", "//"),
    "c": (".c", "//"),
    "csharp": (".cs", "//"),
    "go": (".go", "//"),
    "ruby": (".rb", "#"),
    "swift": (".swift", "//"),
}

USER_AGENT = "github-action-leetcode-sync/1.0 (+https://github.com)"

def sanitize(s: str) -> str:
    s = s.strip()
    s = s.replace(" ", "-")
    s = re.sub(r"[^A-Za-z0-9\-\_]", "", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.lower()

def get_file_ext_and_comment(lang: str):
    lang_lower = lang.lower()
    return LANG_INFO.get(lang_lower, (".txt", "#"))

def fetch_submissions(session: requests.Session, limit: int = 1000):
    results = []
    offset = 0
    page_limit = 50
    while offset < limit:
        url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={page_limit}"
        print(f"Fetching submissions offset={offset} limit={page_limit}")
        r = session.get(url, timeout=30)
        if r.status_code != 200:
            print(f"Failed to fetch submissions: {r.status_code} {r.text[:200]}")
            break
        try:
            data = r.json()
        except Exception as e:
            print("Failed to parse submissions JSON:", e)
            break
        batch = data.get("submissions_dump") or data.get("submissions", [])
        if not batch:
            break
        results.extend(batch)
        if len(batch) < page_limit:
            break
        offset += page_limit
        if offset >= limit:
            break
        time.sleep(0.5)
    print(f"Total submissions fetched: {len(results)}")
    return results

def fetch_submission_code(session: requests.Session, submission_id: int) -> Optional[Dict]:
    graphql_url = "https://leetcode.com/graphql"
    query = """
    query submissionDetail($id: ID!) {
      submissionDetail(submissionId: $id) {
        code
        runtime
        memory
        lang
        timestamp
        question {
          titleSlug
          title
          questionFrontendId
        }
      }
    }
    """
    variables = {"id": str(submission_id)}
    payload = {"query": query, "variables": variables}
    headers = {"Content-Type": "application/json", "User-Agent": USER_AGENT}
    csrftoken = session.cookies.get("csrftoken") or session.cookies.get("CSRFToken")
    if csrftoken:
        headers["x-csrftoken"] = csrftoken
    resp = session.post(graphql_url, json=payload, headers=headers, timeout=30)
    if resp.status_code != 200:
        print(f"GraphQL fetch failed for submission {submission_id}: {resp.status_code}")
        return None
    try:
        body = resp.json()
    except Exception as e:
        print(f"Failed to parse GraphQL JSON for {submission_id}: {e}")
        return None
    data = body.get("data", {})
    sub = data.get("submissionDetail")
    if not sub:
        print(f"No submissionDetail in GraphQL response for {submission_id}: {body}")
        return None
    return sub

def make_header(comment_mark: str, meta: Dict):
    lines = []
    lines.append(f"{comment_mark} LeetCode Problem: {meta.get('title') or meta.get('titleSlug')}")
    if meta.get("questionFrontendId"):
        lines.append(f"{comment_mark} Problem ID: {meta.get('questionFrontendId')}")
    if meta.get("titleSlug"):
        url = f"https://leetcode.com/problems/{meta.get('titleSlug')}/"
        lines.append(f"{comment_mark} URL: {url}")
    if meta.get("lang"):
        lines.append(f"{comment_mark} Language: {meta.get('lang')}")
    if meta.get("timestamp"):
        lines.append(f"{comment_mark} Timestamp: {meta.get('timestamp')}")
    lines.append(f"{comment_mark} Synced by leetcode-sync script")
    return "\n".join(lines) + "\n\n"

def main():
    if not LEETCODE_SESSION:
        print("No LEETCODE_SESSION provided. Exiting without changes.")
        sys.exit(0)

    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Referer": "https://leetcode.com"})
    s.cookies.set("LEETCODE_SESSION", LEETCODE_SESSION, domain="leetcode.com", path="/")

    try:
        resp = s.get("https://leetcode.com", timeout=30)
        if resp.status_code != 200:
            print("Warning: GET https://leetcode.com returned", resp.status_code)
    except Exception as e:
        print("Failed to GET homepage:", e)
        sys.exit(1)

    submissions = fetch_submissions(s, limit=1000)
    if not submissions:
        print("No submissions available or failed to fetch submissions.")
        sys.exit(0)

    files_written = 0
    files_updated = 0
    files_skipped = 0

    for sub in submissions:
        status = sub.get("status_display") or sub.get("status")
        if status != "Accepted":
            continue
        sub_id = sub.get("id")
        title_slug = sub.get("title_slug") or sub.get("titleSlug")
        lang = sub.get("lang") or sub.get("language") or sub.get("language_display") or sub.get("status_lang", "unknown")
        if not sub_id or not title_slug:
            continue

        detail = fetch_submission_code(s, sub_id)
        if not detail:
            print(f"Skipping submission {sub_id} due to fetch failure.")
            continue

        code = detail.get("code") or detail.get("submission_code") or ""
        q = detail.get("question") or {}
        question_slug = q.get("titleSlug") or title_slug
        question_title = q.get("title") or sub.get("title") or title_slug
        question_id = q.get("questionFrontendId") or sub.get("question_id") or sub.get("questionFrontendId")

        ext, comment_mark = get_file_ext_and_comment(lang or (detail.get("lang") or ""))
        safe_slug = sanitize(question_slug)
        safe_title = sanitize(question_title)
        lang_dir = sanitize(lang or detail.get("lang") or "unknown")
        target_dir = OUT_DIR / lang_dir
        target_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{question_id}-{safe_slug}{ext}" if question_id else f"{safe_slug}{ext}"
        target_path = target_dir / filename

        header_meta = {
            "title": question_title,
            "titleSlug": question_slug,
            "questionFrontendId": question_id,
            "lang": lang,
            "timestamp": detail.get("timestamp"),
        }
        header = make_header(comment_mark, header_meta)

        if ext in [".py", ".rb", ".sh", ".txt", ".md", ".java", ".js", ".ts", ".go", ".c", ".cpp", ".cs"]:
            content = header + code.lstrip("\n")
        else:
            content = header + code

        if target_path.exists():
            try:
                existing = target_path.read_text(encoding="utf-8")
            except Exception:
                existing = None
            if existing == content:
                files_skipped += 1
                print(f"Skipped (no change): {target_path}")
                continue
            else:
                print(f"Updating file: {target_path}")
                target_path.write_text(content, encoding="utf-8")
                files_updated += 1
        else:
            print(f"Writing new file: {target_path}")
            target_path.write_text(content, encoding="utf-8")
            files_written += 1

        time.sleep(0.3)

    print(f"Done. Written: {files_written}, Updated: {files_updated}, Skipped: {files_skipped}")
    sys.exit(0)

if __name__ == "__main__":
    main()
