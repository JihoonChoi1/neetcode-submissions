class FreqStack:

    def __init__(self):
        self.freqToVal = defaultdict(list)
        self.valToFreq = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.valToFreq[val] = self.valToFreq.get(val, 0) + 1
        self.freqToVal[self.valToFreq[val]].append(val)
        self.maxFreq = max(self.valToFreq[val], self.maxFreq)

    def pop(self) -> int:
        res = self.freqToVal[self.maxFreq].pop()
        if len(self.freqToVal[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.valToFreq[res] -= 1
        return res





# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()