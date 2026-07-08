class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()

        visited.add((0,0))
        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            if row == rows-1 and col == cols-1:
                return time
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if min(newRow, newCol) < 0 or newRow >= rows or newCol >= cols or (newRow, newCol) in visited:
                    continue
                visited.add((newRow, newCol))
                heapq.heappush(minHeap, (max(time, grid[newRow][newCol]), newRow, newCol))
        
        return -1


            
