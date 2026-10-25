class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+' or c == '-' or c == '*' or c == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                new_val = 0
                if c == '+':
                    new_val = val1 + val2
                elif c == '-':
                    new_val = val2 - val1
                elif c == '*':
                    new_val = val1 * val2
                else:
                    new_val = int(val2 / val1)

                stack.append(new_val)
            else:
                stack.append(int(c))

        return stack[-1]


