class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countsT, window = {}, {}
        for c in t:
            countsT[c] = 1 + countsT.get(c, 0)

        res, resLen = [0, 0], float('inf')
        l = 0
        have = 0
        need = len(countsT)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countsT and window[s[r]] == countsT[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r+1]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in countsT and window[s[l]] < countsT[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]]
                


        


            




                

