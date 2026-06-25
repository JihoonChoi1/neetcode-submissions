class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        minHeap = []

        minHeap = [[cap, prof] for cap, prof in zip(capital, profits)]
        heapq.heapify(minHeap)

        while k > 0:
            while minHeap and minHeap[0][0] <= w:
                cap, prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -prof)
            if maxHeap:
                w += (-1 * heapq.heappop(maxHeap))
            k -= 1
        return w
        
