class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        maxHeap = [[-count, c] for c, count in counts.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = ""

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            count, c = heapq.heappop(maxHeap)
            res += c
            count += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if count != 0:
                prev = [count, c]

        return res