class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtrack(cur, startIdx):
            if startIdx == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(startIdx, len(s)):
                if s[startIdx:j+1] not in wordDict:
                    continue
                cur.append(s[startIdx:j+1])
                backtrack(cur, j+1)
                cur.pop()

        backtrack([], 0)
        return res