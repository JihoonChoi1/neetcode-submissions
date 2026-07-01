class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []
        wordSet = set(wordDict)
        canBreak = [False] * (n + 1)
        canBreak[n] = True
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in wordSet and canBreak[j+1]:
                    canBreak[i] = True
                    break


        def backtrack(cur, startIdx):
            if startIdx == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(startIdx, len(s)):
                if s[startIdx:j+1] in wordSet and canBreak[j+1]:
                    cur.append(s[startIdx:j+1])
                    backtrack(cur, j+1)
                    cur.pop()

        backtrack([], 0)
        return res