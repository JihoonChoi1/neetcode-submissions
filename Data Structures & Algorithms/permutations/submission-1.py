class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True
                    backtrack(perm)
                    perm.pop()
                    used[i] = False

        backtrack([])
        return res


