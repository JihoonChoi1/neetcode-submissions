class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n+1)]
        visited = [False] * (n+1)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        cycleEnd = -1

        def dfs(node, par):
            nonlocal cycleEnd
            if visited[node]:
                cycleEnd = node
                return True
            visited[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleEnd != -1:
                        cycle.add(node)
                    if cycleEnd == node:
                        cycleEnd = -1
                    return True
            return False
            
        dfs(1, -1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
                    
        return []
                    
                    
                    
                
