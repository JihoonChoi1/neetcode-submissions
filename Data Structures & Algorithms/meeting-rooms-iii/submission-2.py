class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = []
        count = [0] * n

        for i in range(n):
            heapq.heappush(available, (0, i))

        for start, end in meetings:
            while available[0][0] < start:
                end_time, roomIdx = heapq.heappop(available)
                heapq.heappush(available, (start, roomIdx))
            
            end_time, roomIdx = heapq.heappop(available)
            heapq.heappush(available, (end_time + (end - start), roomIdx))
            count[roomIdx] += 1

        return count.index(max(count))
