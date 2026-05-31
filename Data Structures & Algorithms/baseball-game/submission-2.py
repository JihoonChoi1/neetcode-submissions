class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == "+":
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                stack.append(stack[-1] * 2)
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))
        res = 0
        for num in stack:
            res += num
        return res

