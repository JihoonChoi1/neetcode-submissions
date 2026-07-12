class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n < 3:
            if n == 0:
                return t0
            return 1

        for _ in range(n-2):
            tmp1 = t1
            tmp2 = t2
            t2 = t0 + t1 + t2
            t1 = tmp2
            t0 = tmp1

        return t2




