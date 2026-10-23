class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = r = 0
        currMax = 0
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            currMax = max(currMax, count[s[r]])

            while ((r-l+1) - currMax > k):
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res

        
