class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xfff
        intMax = 0x7ff

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= intMax else ~(a ^ mask)


