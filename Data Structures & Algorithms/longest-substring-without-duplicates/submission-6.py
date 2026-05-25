class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        chars = {}
        while r < len(s):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            res = max(res, r-l+1)
            chars[s[r]] = r
            r += 1
        return res
