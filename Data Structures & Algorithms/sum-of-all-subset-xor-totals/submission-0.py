class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, subset):
            nonlocal res
            xxor = 0
            for num in subset:
                xxor ^= num
            res += xxor

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res

