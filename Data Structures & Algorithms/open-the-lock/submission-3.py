class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        if target in deadends:
            return -1

        visited = set(deadends)
        begin = {"0000"}
        end = {target}
        steps = 0
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            steps += 1
            temp = set()
            for lock in begin:
                for i in range(4):
                    for j in [-1,1]:
                        digit = (int(lock[i]) + j + 10) % 10
                        nextLock = lock[:i] + str(digit) + lock[i+1:]
                        if nextLock in end:
                            return steps
                        if nextLock in visited:
                            continue
                        visited.add(nextLock)
                        temp.add(nextLock)
            begin = temp
        return -1   
                    




