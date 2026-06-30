class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(cur, i):
            if i == len(digits):
                if cur:
                    res.append("".join(cur))
                return

            chars = digitToChar[digits[i]]
            for c in chars:
                cur.append(c)
                backtrack(cur, i+1)
                cur.pop()

        backtrack([], 0)
        return res
