class UnionFind:
    def __init__(self, n):
        self.numOfIsland = n
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        self.numOfIsland -= 1
        if self.size[pa] < self.size[pb]:
            self.size[pb] += self.size[pa]
            self.par[pa] = pb
        else:
            self.size[pa] += self.size[pb]
            self.par[pb] = pa
        return True

    def isConnected(self):
        return self.numOfIsland == 1




class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e: e[2])

        def findMST(index, include):
            uf = UnionFind(n)
            totalWgt = 0
            if include:
                totalWgt += edges[index][2]
                uf.union(edges[index][0], edges[index][1])

            for i, edge in enumerate(edges):
                if i == index:
                    continue
                if uf.union(edge[0], edge[1]):
                    totalWgt += edge[2]

            return totalWgt if uf.isConnected() else float('inf')

        minWeight = findMST(-1, False)
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if minWeight < findMST(i, False):
                critical.append(e[3])
            elif minWeight == findMST(i, True):
                pseudo.append(e[3])

        return [critical, pseudo]


















