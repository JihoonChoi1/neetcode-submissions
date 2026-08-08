class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for _ in range(32):
            if 1 & n:
                res += 1
            n >>= 1
        return res