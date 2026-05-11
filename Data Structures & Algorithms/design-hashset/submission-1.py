class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10007)]

    def add(self, key: int) -> None:
        bucket = self.buckets[hash(key) % 10007]
        if key not in bucket:
            self.buckets[hash(key) % 10007].append(key)

    def remove(self, key: int) -> None:
        try:
            self.buckets[hash(key) % 10007].remove(key)
        except ValueError:
            pass


    def contains(self, key: int) -> bool:
        bucket = self.buckets[hash(key) % 10007]
        for val in bucket:
            if val == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)