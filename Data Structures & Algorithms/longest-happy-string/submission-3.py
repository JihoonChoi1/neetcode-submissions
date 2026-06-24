class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, [count, char])

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                newCount, newChar = heapq.heappop(maxHeap)
                newCount += 1
                res += newChar
                if newCount < 0:
                    heapq.heappush(maxHeap, [newCount, newChar])
            else:
                res += char
                count += 1
            if count < 0:
                heapq.heappush(maxHeap, [count, char])

        return res
            