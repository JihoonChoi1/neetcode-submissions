class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = nums[0]


        for num in nums:
            tmp = currMax * num

            currMax = max(tmp, currMin * num, num)
            currMin = min(tmp, currMin * num, num)

            res = max(currMax, res)

        return res