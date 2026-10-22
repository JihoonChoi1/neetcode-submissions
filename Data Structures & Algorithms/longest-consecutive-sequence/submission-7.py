class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        vals = set()

        for num in nums:
            vals.add(num)

        res = 1

        for num in vals:
            if num-1 in vals:
                continue
            
            tmp = 1
            while num+1 in vals:
                tmp += 1
                res = max(res, tmp)
                num += 1

        return res
            
            

            