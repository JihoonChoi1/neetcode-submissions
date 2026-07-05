class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nei in adj[node]:
                isPrereq[nei].add(node)
                isPrereq[nei].update(isPrereq[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return [u in isPrereq[v] for u,v in queries]