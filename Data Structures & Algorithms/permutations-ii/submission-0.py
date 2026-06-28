class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        nums.sort()
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    perm.append(nums[i])
                    backtrack()
                    used[i] = False
                    perm.pop()
        
        backtrack()
        return res


                
