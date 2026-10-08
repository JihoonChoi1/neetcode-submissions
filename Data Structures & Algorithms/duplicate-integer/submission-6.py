class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mark = set()
        for num in nums:
            if num in mark:
                return True
            mark.add(num)
        return False