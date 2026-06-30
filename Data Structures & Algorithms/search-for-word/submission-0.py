class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowSize = len(board)
        colSize = len(board[0])

        def backtrack(row, col, wordIdx):
            if wordIdx == len(word):
                return True
            if (row < 0 or row >= rowSize or col < 0 or col >= colSize 
                or board[row][col] != word[wordIdx] or board[row][col] == "#"):
                return False

            board[row][col] = "#"

            res = (backtrack(row-1, col, wordIdx+1) or
                   backtrack(row+1, col, wordIdx+1) or
                   backtrack(row, col-1, wordIdx+1) or
                   backtrack(row, col+1, wordIdx+1))
            
            board[row][col] = word[wordIdx]

            return res

        for r in range(rowSize):
            for c in range(colSize):
                if backtrack(r, c, 0):
                    return True
        return False
            


                    
