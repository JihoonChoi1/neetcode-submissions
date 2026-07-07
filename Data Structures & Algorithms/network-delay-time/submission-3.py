class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for _ in range(n+1)]

        for ui,vi,ti in times:
            adj[ui].append((ti, vi))

        visited = {k}

        minHeap = adj[k]

        heapq.heapify(minHeap)

        while minHeap:
            time, nei = heapq.heappop(minHeap)
            if nei in visited:
                continue
            visited.add(nei)
            if len(visited) == n:
                return time
            for ti, vi in adj[nei]:
                heapq.heappush(minHeap, (time+ti, vi))
        
        return -1

