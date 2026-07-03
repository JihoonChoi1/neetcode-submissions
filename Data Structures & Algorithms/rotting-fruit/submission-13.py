class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        fresh = 0
        q = deque()

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        res = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rowLen and 0 <= nc < colLen and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            res += 1
        
        return -1 if fresh > 0 else res


