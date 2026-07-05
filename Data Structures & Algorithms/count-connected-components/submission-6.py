class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = [set() for _ in range(n)]
        visited = [False] * n

        for e1, e2 in edges:
            graphMap[e1].add(e2)
            graphMap[e2].add(e1)

        def bfs(edge):
            q = deque([edge])
            visited[edge] = True
            while q:
                node = q.popleft()
                for adj in graphMap[node]:
                    if not visited[adj]:
                        visited[adj] = True
                        q.append(adj)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)

        return count
