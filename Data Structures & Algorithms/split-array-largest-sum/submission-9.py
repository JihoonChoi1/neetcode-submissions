class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest: int) -> bool:
            numArray = 1
            total = 0
            for num in nums:
                if total + num > largest:
                    numArray += 1
                    total = 0
                total += num
            return numArray <= k


        l, r = max(nums), sum(nums)
        res = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res