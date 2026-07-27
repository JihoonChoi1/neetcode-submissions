class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[0])
        prevEnd = intervals[0][1]
        n = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < prevEnd:
                prevEnd = min(prevEnd, end)
                n += 1
            else:
                prevEnd = end

        return n