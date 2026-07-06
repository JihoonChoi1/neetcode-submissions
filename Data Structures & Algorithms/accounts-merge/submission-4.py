class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        par1 = self.find(x1)
        par2 = self.find(x2)
        if par1 == par2:
            return
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        return
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAcc = {}
        uf = UnionFind(len(accounts))


        for i, emails in enumerate(accounts):
            emails = emails[1:]
            for email in emails:
                if email in emailToAcc:
                    uf.union(emailToAcc[email], i)
                else:
                    emailToAcc[email] = i

        
        accToEmail = defaultdict(list)
        for e, i in emailToAcc.items():
            accToEmail[uf.find(i)].append(e)
        
        res = []
        for acc, emails in accToEmail.items():
            res.append([accounts[acc][0]] + sorted(emails))

        return res
    