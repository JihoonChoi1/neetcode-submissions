class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max = len(nums) + 1
        hasOne = False
        for i in range(len(nums)):
            if nums[i] == 1:
                hasOne = True
            if nums[i] >= max or nums[i] < 1:
                nums[i] = 1
        if not hasOne:
            return 1
        for i in range(max - 1):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
        for i in range(max - 1):
            if nums[i] > 0:
                return i + 1
        return max 
