class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(n)]

        def dfs(i, firstRobbed):
            if i >= n or (firstRobbed and i == n-1):
                return 0

            if memo[i][firstRobbed] != -1:
                return memo[i][firstRobbed]

            memo[i][firstRobbed] = max(dfs(i+1, firstRobbed), nums[i] + dfs(i+2, firstRobbed))

            return memo[i][firstRobbed]

        return max(dfs(0, True), dfs(1, False))

            