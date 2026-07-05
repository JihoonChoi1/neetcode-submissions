class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for pre, crs in prerequisites:
            isPrereq[pre][crs] = 1
            adj[crs].append(pre)


        def dfs(prereq, crs):
            if isPrereq[prereq][crs] != -1:
                return isPrereq[prereq][crs] == 1

            for pre in adj[crs]:
                if isPrereq[prereq][pre] == 1 or dfs(prereq, pre):
                    isPrereq[prereq][crs] = 1
                    return True

            isPrereq[prereq][crs] = 0
            return False


        res = []
        for pre, crs in queries:
            res.append(dfs(pre, crs))

        return res
            
