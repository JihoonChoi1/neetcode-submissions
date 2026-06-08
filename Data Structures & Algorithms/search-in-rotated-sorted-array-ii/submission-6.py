class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            while(l < n-1 and nums[l] == nums[l + 1]):
                l += 1
            while(r > 0 and nums[r] == nums[r-1]):
                r -= 1
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

