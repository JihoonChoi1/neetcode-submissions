class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        adj = [[] for _ in range(n)]
        indegree = [0] * (n)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        q = deque()

        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        
        remaining = n
        while remaining > 2:
            for _ in range(len(q)):
                node = q.popleft()
                remaining -= 1
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return list(q)
        




        