class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        numOfRows, numOfCols = len(grid), len(grid[0])
        visited = set()

        def dfs(rowIdx, colIdx):
            if rowIdx < 0 or colIdx < 0 or rowIdx == numOfRows or colIdx == numOfCols or not grid[rowIdx][colIdx]:
                return 1
            if (rowIdx, colIdx) in visited:
                return 0

            visited.add((rowIdx, colIdx))
            perimeter = dfs(rowIdx-1, colIdx) + dfs(rowIdx+1, colIdx) + dfs(rowIdx, colIdx-1) + dfs(rowIdx, colIdx+1)

            return perimeter

        for i in range(numOfRows):
            for j in range(numOfCols):
                if grid[i][j]:
                    return dfs(i,j)
