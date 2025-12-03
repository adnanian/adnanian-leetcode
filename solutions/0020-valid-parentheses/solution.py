bracket_map = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Solution:
    def isValid(self, s: str) -> bool:
        open_stack: List[str] = []
        for bracket in s:
            if bracket not in bracket_map.keys():
                if open_stack and bracket_map[open_stack[-1]] == bracket:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(bracket)
        return not open_stack
