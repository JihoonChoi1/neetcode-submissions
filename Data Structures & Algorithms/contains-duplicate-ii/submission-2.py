class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        L = 0
        R = 0
        for num in nums:
            if R - L > k:
                win.remove(nums[L])
                L += 1
            if num in win:
                return True
            win.add(nums[R])
            R += 1
        return False




