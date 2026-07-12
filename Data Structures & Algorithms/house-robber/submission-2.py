class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        maxi = [0] * n

        maxi[0] = nums[0]
        maxi[1] = max(nums[0], nums[1])

        for i in range(2, n):
            maxi[i] = max(maxi[i-1], maxi[i-2] + nums[i])

        return maxi[-1]

