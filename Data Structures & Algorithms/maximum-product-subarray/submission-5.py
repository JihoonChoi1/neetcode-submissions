class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = nums[0]

        for num in nums:
            tmp = curMax*num
            curMax = max(curMax*num, num*curMin, num)
            curMin = min(tmp, num*curMin, num)
            res = max(res, curMax)

        return res