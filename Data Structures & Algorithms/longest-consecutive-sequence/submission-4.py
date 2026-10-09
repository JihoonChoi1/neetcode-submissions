class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        if len(nums) == 0:
            return 0
            
        for num in nums:
            numbers.add(num)

        res = 1
        
        for num in numbers:
            count = 1
            if num-1 not in numbers:
                while num+1 in numbers:
                    count += 1
                    num += 1
                res = max(count, res)
            
        return res