class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsCount = len(nums)
        prefix = [1] * numsCount
        suffix = [1] * numsCount


        prefix[0] = 1
        for i in range(1, numsCount):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix[numsCount - 1] = 1
        for i in range(numsCount - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        return [prefix[i] * suffix[i] for i in range(numsCount)]
        