class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def dfs(cur, target, visited):
            if cur not in adj or target not in adj:
                return -1
            if cur == target:
                return 1

            visited.add(cur)

            for nei, val in adj[cur]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return val * result
            return -1

        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res
                

            
