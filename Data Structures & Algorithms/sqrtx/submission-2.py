class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        m = 0
        while l < r:
            m = (l + r) // 2
            squareM = m * m
            if squareM == x:
                return m
            elif squareM < x:
                l = m + 1
            else:
                r = m - 1
        if l * l > x:
            return l - 1
        return l