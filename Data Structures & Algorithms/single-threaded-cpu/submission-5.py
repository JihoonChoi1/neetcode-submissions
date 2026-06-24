class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waitminHeap = [[enqueueTime, processingTime, i] for i, [enqueueTime, processingTime] in enumerate(tasks)]
        waitminHeap.sort()
        curTime = 1
        processminHeap = []
        res = []

        while waitminHeap or processminHeap:
            while waitminHeap and waitminHeap[0][0] <= curTime:
                enqueueTime, processingTime, i = heapq.heappop(waitminHeap)
                heapq.heappush(processminHeap, [processingTime, enqueueTime, i])
            if processminHeap:
                task = heapq.heappop(processminHeap)
                curTime += task[0]
                res.append(task[2])
            else:
                if waitminHeap:
                    curTime = waitminHeap[0][0]
        return res