class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0 # Start index
        j = len(needle) # End index
        while i < len(haystack) and j < len(haystack) + 1:
            if haystack[i:j] == needle:
                return i
            i += 1
            j += 1
        return -1
