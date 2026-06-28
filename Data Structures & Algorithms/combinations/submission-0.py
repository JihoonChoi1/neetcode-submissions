class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(cur, num):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for num in range(num, n+1):
                cur.append(num)
                dfs(cur, num+1)
                cur.pop()
        
        dfs([], 1)
        return res


