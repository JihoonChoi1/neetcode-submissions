class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(rowIdx):
            nonlocal res
            if rowIdx == n:
                res += 1
                return
            
            for colIdx in range(n):
                if colIdx in cols or rowIdx-colIdx in diag1 or rowIdx+colIdx in diag2:
                    continue
                cols.add(colIdx)
                diag1.add(rowIdx-colIdx)
                diag2.add(rowIdx+colIdx)

                backtrack(rowIdx + 1)

                cols.remove(colIdx)
                diag1.remove(rowIdx-colIdx)
                diag2.remove(rowIdx+colIdx)

            
        backtrack(0)
        return res


                