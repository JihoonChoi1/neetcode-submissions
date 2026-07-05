class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        q = deque()

        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []

        finished = 0
        while q:
            course = q.popleft()
            res.append(course)
            for dest in adj[course]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    q.append(dest)
            finished += 1
        
        return res if finished == numCourses else []
            
