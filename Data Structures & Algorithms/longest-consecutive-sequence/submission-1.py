class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        elements = set()
        for num in nums:
            elements.add(num)
        for num in nums:
            if num - 1 in elements:
                continue
            tmp = 1
            while num + 1 in elements:
                tmp += 1
                num += 1
            if tmp > res:
                res = tmp
        return res
            

