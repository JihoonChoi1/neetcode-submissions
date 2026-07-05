class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrereq = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            isPrereq[pre][crs] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    isPrereq[i][j] = isPrereq[i][j] or (isPrereq[i][k] and isPrereq[k][j])
        
        return [isPrereq[pre][crs] for pre, crs in queries]

        