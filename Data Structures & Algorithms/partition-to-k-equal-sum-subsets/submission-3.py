class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = [0] * k
        numsTotal = sum(nums)
        nums.sort(reverse=True)
        if numsTotal % k:
            return False
        limit = numsTotal // k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if subsets[j] + nums[i] <= limit:
                    subsets[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    subsets[j] -= nums[i]
                if subsets[j] == 0:
                    break
            return False

        return backtrack(0)
                    
                    
                