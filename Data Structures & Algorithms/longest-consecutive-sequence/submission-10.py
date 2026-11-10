class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = set()
        for num in nums:
            count.add(num)

        res = 1

        for num in count:
            if num - 1 in count:
                continue

            curr = num
            candRes = 1
            while curr + 1 in count:
                candRes += 1
                curr += 1
            res = max(res, candRes)

        return res