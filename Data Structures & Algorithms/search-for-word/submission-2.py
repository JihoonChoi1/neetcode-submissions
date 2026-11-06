class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or board[row][col] != word[i]:
                return False
            board_val = board[row][col]
            board[row][col] = '#'

            res = dfs(row-1, col, i+1) or dfs(row+1, col, i+1) or dfs(row, col-1, i+1) or dfs(row, col+1, i+1)

            board[row][col] = board_val

            return res
            
            



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return  True
        return False