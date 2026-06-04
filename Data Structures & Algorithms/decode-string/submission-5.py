class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for c in s:
            if c == "]":
                curr = ""
                while stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                stack.append(int(count) * curr)
            else:
                stack.append(c)
        return "".join(stack)


