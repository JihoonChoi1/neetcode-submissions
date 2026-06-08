class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.vals[key]
        l = 0
        r = len(tmp) - 1
        res = ""
        while l <= r:
            mid = l + ((r - l) // 2)
            if tmp[mid][1] == timestamp:
                return tmp[mid][0]
            if tmp[mid][1] < timestamp:
                res = tmp[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
            

