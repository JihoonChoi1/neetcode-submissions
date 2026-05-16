class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = 0
        partialSums = defaultdict(int)
        partialSums[0] = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum - k in partialSums:
                counts += partialSums[currSum - k]
            partialSums[currSum] += 1
        return counts
