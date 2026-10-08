class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]

        for j in range(n - 2, -1, -1):
            suff[j] = suff[j+1] * nums[j+1]

        res = []
        for i in range(n):
            res.append(pre[i] * suff[i])

        return res

            
            
                