class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10007)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[hash(key) % 10007]
        for i, (k,v) in enumerate(bucket):
            if(k == key):
                bucket[i] = (k,value)
                return
        bucket.append((key,value))
        return

    def get(self, key: int) -> int:
        bucket = self.buckets[hash(key) % 10007]
        for i, (k,v) in enumerate(bucket):
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        bucket = self.buckets[hash(key) % 10007]
        for i, (k,v) in enumerate(bucket):
            if key == k:
                bucket.remove((k,v))
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)