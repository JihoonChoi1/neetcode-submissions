class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        arr = [[] for _ in range(len(nums) + 1)]
        for a,b in counts.items():
            arr[b].append(a)
        for x in arr[::-1]:
            if len(x) != 0:
                for a in x:
                    res.append(a)
                    k -= 1
                    if k == 0:
                        return res
        return res
        
