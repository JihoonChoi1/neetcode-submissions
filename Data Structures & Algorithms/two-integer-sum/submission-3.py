class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            val = check.get(target - num)
            if val is not None:
                return [val, i]
            check[num] = i
        return False
