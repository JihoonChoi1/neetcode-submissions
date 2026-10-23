class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = 0
        for pile in piles:
            maxRate = max(maxRate, pile)

        minRate = 1
        res = maxRate

        while minRate <= maxRate:
            midRate = minRate + (maxRate-minRate) // 2
            currHour = 0
            for pile in piles:
                currHour += (pile + midRate - 1) // midRate
            if currHour <= h:
                res = min(res, midRate)
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
        
        return res