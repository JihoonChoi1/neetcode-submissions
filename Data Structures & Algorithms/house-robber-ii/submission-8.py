class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            cost = [0] * n
            cost[0] = arr[0]
            cost[1] = max(arr[0], arr[1])

            for i in range(2, n):
                cost[i] = max(cost[i-1], arr[i] + cost[i-2])

            return cost[-1]


        
        return max(helper(nums[1:]), helper(nums[:-1]))

        
