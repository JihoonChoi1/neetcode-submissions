class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.Size = [1 for _ in range(n)]

    def find(self, num):
        while self.par[num] != num:
            self.par[num] = self.par[self.par[num]]
            num = self.par[num]
        return num

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.n -= 1
        if self.Size[pu] < self.Size[pv]:
            self.par[pu] = pv
            self.Size[pv] += self.Size[pu]
        else:
            self.par[pv] = pu
            self.Size[pu] += self.Size[pv]
        return True

    def isConnected(self):
        return self.n == 1



class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor_index = {}


        for i,n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i

        return uf.isConnected()
                    















