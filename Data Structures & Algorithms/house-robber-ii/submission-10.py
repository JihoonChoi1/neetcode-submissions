class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                tmp = prev1
                prev1 = max(prev1, num + prev2)
                prev2 = tmp

            return prev1


        
        return max(helper(nums[1:]), helper(nums[:-1]))

        
