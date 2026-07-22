class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        memo = {}

        def dfs(r, c, prev):
            if min(r,c) < 0 or r >= rowLen or c >= colLen or matrix[r][c] <= prev:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            pathLen = 0
            pathLen = max(pathLen, 1 + dfs(r-1, c, matrix[r][c]))
            pathLen = max(pathLen, 1 + dfs(r+1, c, matrix[r][c]))
            pathLen = max(pathLen, 1 + dfs(r, c-1, matrix[r][c]))
            pathLen = max(pathLen, 1 + dfs(r, c+1, matrix[r][c]))

            memo[(r,c)] = pathLen

            return memo[(r,c)]

        for i in range(rowLen):
            for j in range(colLen):
                dfs(i, j, -1)
        
        return max(memo.values())





