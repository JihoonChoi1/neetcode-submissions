class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            m = (l + r) // 2
            squareM = m * m
            if squareM == x:
                return m
            elif squareM < x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res