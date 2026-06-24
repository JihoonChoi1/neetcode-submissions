class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = trips[0][1], trips[0][2]
        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)

        N = R - L + 1
        passChange = [0] * N
        for numPass, start, end in trips:
            passChange[start-L] += numPass
            passChange[end-L] -= numPass
        
        curPass = 0

        for i in range(len(passChange)):
            curPass += passChange[i]
            if curPass > capacity:
                return False
        return True
