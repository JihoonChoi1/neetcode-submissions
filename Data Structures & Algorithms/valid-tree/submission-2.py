class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        neighbors = defaultdict(list)

        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in neighbors[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n
        
        


