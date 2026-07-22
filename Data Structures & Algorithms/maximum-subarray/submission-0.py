class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        res = curMax
        for i in range(1, len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            res = max(res, curMax)
        return res
