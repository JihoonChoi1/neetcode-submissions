class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        
        pac = set()
        atl = set()


        def dfs(i, j, visited, prevVal):
            if (i, j) in visited or i < 0 or j < 0 or i >= ROW or j >= COL or prevVal > heights[i][j]:
                return
            
            visited.add((i, j))

            dfs(i-1, j, visited, heights[i][j])
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])

        

        for i in range(ROW):
            dfs(i, 0, pac, 0)
            dfs(i, COL-1, atl, 0)

        for j in range(COL):
            dfs(0, j, pac, 0)
            dfs(ROW-1, j, atl, 0)


        res = []

        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res

        
            





        


        

