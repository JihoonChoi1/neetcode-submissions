class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            daysNeeded = 1
            capacity = l + ((r - l) // 2)
            weightLoaded = 0
            for i in range(len(weights)):
                if capacity - weightLoaded < weights[i]:
                    daysNeeded += 1
                    weightLoaded = 0
                weightLoaded += weights[i]
            if daysNeeded > days:
                l = capacity + 1
            else:
                res = min(res, capacity)
                r = capacity - 1
        return res
        