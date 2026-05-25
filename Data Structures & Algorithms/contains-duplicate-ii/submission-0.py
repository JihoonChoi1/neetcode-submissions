class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = {}
        for i, num in enumerate(nums):
            if num in vals:
                if abs(i-vals[num]) <= k:
                    return True
            vals[num] = i
        return False



