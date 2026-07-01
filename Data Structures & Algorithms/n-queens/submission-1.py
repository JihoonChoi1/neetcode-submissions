class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(rowIdx):
            if rowIdx == n:
                res.append(["".join(board[i]) for i in range(n)])
                return
            for colIdx in range(n):
                if colIdx in cols or rowIdx-colIdx in diag1 or rowIdx+colIdx in diag2:
                    continue
                board[rowIdx][colIdx] = "Q"
                cols.add(colIdx)
                diag1.add(rowIdx-colIdx)
                diag2.add(rowIdx+colIdx)
                backtrack(rowIdx+1)
                board[rowIdx][colIdx] = "."
                cols.remove(colIdx)
                diag1.remove(rowIdx-colIdx)
                diag2.remove(rowIdx+colIdx)
        
        backtrack(0)
        return res

            
