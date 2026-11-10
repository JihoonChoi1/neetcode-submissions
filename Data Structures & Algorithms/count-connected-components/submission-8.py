class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, parent):
            nonlocal visited
            if node in visited:
                return
            visited.add(node)
            for curr in adj[node]:
                if curr == parent:
                    continue
                dfs(curr, node)    

            return
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)
            
        return res


        


