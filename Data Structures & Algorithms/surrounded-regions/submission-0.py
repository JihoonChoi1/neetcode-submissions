class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowLen = len(board)
        colLen = len(board[0])

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= rowLen or 
            col >= colLen or board[row][col] != "O"):
                return
            board[row][col] = "T"
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(rowLen):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][colLen-1] == "O":
                dfs(i, colLen-1)

        for i in range(colLen):
            if board[0][i] == "O":
                dfs(0, i)
            if board[rowLen-1][i] == "O":
                dfs(rowLen-1, i)

        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

        

            
