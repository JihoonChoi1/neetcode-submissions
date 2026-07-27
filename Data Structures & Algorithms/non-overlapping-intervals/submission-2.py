class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[0])
        tmp = [intervals[0][0], intervals[0][1]]
        n = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            lastEnd = tmp[1]
            if start < lastEnd:
                tmp[1] = min(lastEnd, end)
                n += 1
            else:
                tmp = [start, end]

        return n