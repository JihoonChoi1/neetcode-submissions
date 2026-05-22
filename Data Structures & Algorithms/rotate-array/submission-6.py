class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l: int, r: int, nums: List[int]):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums

        s = len(nums)
        k = k % s
        if k == 0: return
        nums = reverse(0, s-1, nums)
        nums = reverse(0, k-1, nums)
        nums = reverse(k, s-1, nums)