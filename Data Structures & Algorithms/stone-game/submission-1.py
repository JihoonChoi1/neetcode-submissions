class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]

        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                pick_left = piles[l] - dp[l + 1][r]
                pick_right = piles[r] - dp[l][r - 1]
                
                dp[l][r] = max(pick_left, pick_right)
                
        return dp[0][n - 1] > 0