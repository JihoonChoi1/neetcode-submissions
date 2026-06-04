class FreqStack:

    def __init__(self):
        self.freqToVal = [[]]
        self.valToFreq = {}

    def push(self, val: int) -> None:
        valCount  = self.valToFreq.get(val, 0) + 1
        self.valToFreq[val] = valCount
        if valCount == len(self.freqToVal):
            self.freqToVal.append([])
        self.freqToVal[valCount].append(val)

    def pop(self) -> int:
        res = self.freqToVal[-1].pop()
        if not self.freqToVal[-1]:
            self.freqToVal.pop()
        self.valToFreq[res] -= 1
        return res