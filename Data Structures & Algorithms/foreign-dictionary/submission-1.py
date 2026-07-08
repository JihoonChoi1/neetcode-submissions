class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        q = deque()
        for c in adj:
            if indegree[c] == 0:
                q.append(c)
        
        res = []

        while q:
            for _ in range(len(q)):
                c = q.popleft()
                res.append(c)
                for nei in adj[c]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return "".join(res) if len(adj) == len(res) else ""




