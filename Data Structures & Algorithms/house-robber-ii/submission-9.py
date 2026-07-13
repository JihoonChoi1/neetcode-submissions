class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])

            for i in range(2, n):
                tmp = prev1
                prev1 = max(prev1, arr[i] + prev2)
                prev2 = tmp

            return prev1


        
        return max(helper(nums[1:]), helper(nums[:-1]))

        
