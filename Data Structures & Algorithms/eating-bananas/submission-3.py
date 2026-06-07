class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        res = r
        while l <= r:
            hoursNeeded = 0
            eatRate = l + ((r-l) // 2)
            for num in piles:
                hoursNeeded += num // eatRate
                if num % eatRate > 0:
                    hoursNeeded += 1
            if hoursNeeded > h:
                l = eatRate + 1
            else:
                res = min(res, eatRate)
                r = eatRate - 1
        return res
