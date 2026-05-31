class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for c in operations:
            if c == "+":
                stack.append(stack[-1] + stack[-2])
                res += stack[-1]
            elif c == "D":
                stack.append(stack[-1] * 2)
                res += stack[-1]
            elif c == "C":
                res -= stack.pop()
            else:
                stack.append(int(c))
                res += stack[-1]
        return res

