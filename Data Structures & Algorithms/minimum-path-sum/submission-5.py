class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [0] * (n+1)
        dp[n-1] = grid[m-1][n-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i == m-1:
                    dp[j] = dp[j+1] + grid[i][j]
                if j == n-1:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j+1])

        return dp[0]