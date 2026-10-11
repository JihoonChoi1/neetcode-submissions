class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        visited = set()

        while r < len(s):
            if s[r] in visited:
                while s[r] in visited:
                    visited.discard(s[l])
                    l += 1
            visited.add(s[r])
            res = max(res, r-l+1)
            r += 1

        return res


