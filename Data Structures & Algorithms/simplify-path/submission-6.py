class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for c in path + "/":
            if c == "/":
                if stack and curr == "..":
                    stack.pop()
                elif curr != "" and curr != ".." and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)
                    

