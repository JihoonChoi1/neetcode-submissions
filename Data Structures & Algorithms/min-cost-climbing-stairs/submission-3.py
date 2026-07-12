class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1 = cost[0]
        prev2 = cost[1]

        for i in range(2, n):
            tmp = prev2
            prev2 = min(prev1, prev2) + cost[i]
            prev1 = tmp

        return min(prev1, prev2)