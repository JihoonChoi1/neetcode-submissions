class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                if num in box[i//3 * 3 + j//3]:
                    return False
                box[i//3 * 3 + j//3].add(num)
                if num in row[i]:
                    return False
                row[i].add(num)
                if num in col[j]:
                    return False
                col[j].add(num)
        return True