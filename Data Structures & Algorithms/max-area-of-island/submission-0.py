class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            return 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)

        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res