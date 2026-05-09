class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in check:
                return [check[val], i]
            check[num] = i
        return []
