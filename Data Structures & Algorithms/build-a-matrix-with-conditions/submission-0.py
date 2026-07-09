class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            adj = [[] for _ in range(k+1)]
            inorder = [0] * (k+1)

            for a,b in edges:
                adj[a].append(b)
                inorder[b] += 1

            q = deque()
            for i in range(1, k+1):
                if inorder[i] == 0:
                    q.append(i)

            res = []
            while q:
                num = q.popleft()
                res.append(num)
                for nei in adj[num]:
                    inorder[nei] -= 1
                    if inorder[nei] == 0:
                        q.append(nei)
            return res

        row_order = topo_sort(rowConditions)
        if len(row_order) != k: return []

        col_order = topo_sort(colConditions)
        if len(col_order) != k: return []

        col_idx = [0] * (k+1)
        for i in range(k):
            col_idx[col_order[i]] = i

        res = [[0] * k for _ in range(k)]

        for i in range(k):
            res[i][col_idx[row_order[i]]] = row_order[i]

        return res


