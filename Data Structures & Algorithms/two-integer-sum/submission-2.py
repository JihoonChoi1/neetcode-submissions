class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            if check.get(target - num) is not None:
                return [check.get(target - num), i]
            check[num] = i
        return False
