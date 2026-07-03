class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or grid[row][col] == "0" or (row,col) in visited:
                return

            visited.add((row,col))

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)


           
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == "1" and (i,j) not in visited:
                    res += 1
                    dfs(i, j)

        return res


            
        