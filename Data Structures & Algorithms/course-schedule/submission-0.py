class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range(numCourses)}

        for i,j in prerequisites:
            premap[i].append(j)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not premap[course]:
                return True
            
            visited.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            premap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

        