class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = [set() for _ in range(n)]
        visited = set()

        for e1, e2 in edges:
            graphMap[e1].add(e2)
            graphMap[e2].add(e1)

        def dfs(edge):
            stack = [edge]
            visited.add(edge)
            while stack:
                node = stack.pop()
                for adj in graphMap[node]:
                    if adj not in visited:
                        visited.add(adj)
                        stack.append(adj)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
