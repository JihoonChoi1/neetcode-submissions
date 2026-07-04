class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(row, col, visited, prevHeight):
            if (min(row,col) < 0 or row >= rowLen or col >= colLen 
                or (row,col) in visited or 
            prevHeight > heights[row][col]):
                return
            visited.add((row,col))
            dfs(row-1, col, visited, heights[row][col])
            dfs(row+1, col, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])

        for col in range(colLen):
            dfs(0, col, pacific, 0)
            dfs(rowLen-1, col, atlantic, 0)

        for row in range(rowLen):
            dfs(row, 0, pacific, 0)
            dfs(row, colLen-1, atlantic, 0)

        for i in range(rowLen):
            for j in range(colLen):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        
        return res


