class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]

        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            finished += 1
            course = q.pop()
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finished == numCourses:
            return True
        return False