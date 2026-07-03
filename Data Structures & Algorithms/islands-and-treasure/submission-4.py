class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowLen = len(grid)
        colLen = len(grid[0])
        q = deque()
        visited = set()

        def addCell(row, col):
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or (row,col) in visited or  grid[row][col] == -1:
                return
            q.append((row, col))
            visited.add((row, col))
        

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row-1, col)
                addCell(row+1, col)
                addCell(row, col-1)
                addCell(row, col+1)
            dist += 1
        return
                
