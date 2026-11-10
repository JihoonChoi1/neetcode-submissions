class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            prev2 = 0
            prev1 = 0

            for i in range(len(arr)):
                temp = max(prev2 + arr[i], prev1)
                prev2 = prev1
                prev1 = temp

            return prev1

        return max(helper(nums[1:]), helper(nums[:-1]))

        
