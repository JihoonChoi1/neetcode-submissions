class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]

        visited = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        q = deque([(0, -1)])

        while q:
            nodeNum, par = q.popleft()
            visited.add(nodeNum)
            for connectedNode in adj[nodeNum]:
                if connectedNode == par:
                    continue
                if connectedNode in visited:
                    return False
                q.append((connectedNode, nodeNum))
        
        return True if len(visited) == n else False
        
                

