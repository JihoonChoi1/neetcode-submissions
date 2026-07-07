class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        minHeap = [[0, 0, 0]]
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visit:
                continue
            if row == rows-1 and col == cols-1:
                return diff
            visit.add((row, col))
            for dr, dc in directions:
                newRow, newCol = row + dr, col+dc
                if newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols or (newRow, newCol) in visit:
                    continue
                newdiff = max(diff, abs(heights[row][col] - heights[newRow][newCol]))
                heapq.heappush(minHeap, (newdiff, newRow, newCol))
            


        