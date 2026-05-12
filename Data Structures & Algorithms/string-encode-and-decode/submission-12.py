class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += f"{len(str)}#{str}"
        return res
    def decode(self, s: str) -> List[str]:
        strs = []
        curr = 0
        i = 0
        while i < len(s):
            size = 0
            j = i
            while s[i] != '#':
                i += 1
            size = int(s[j:i])
            word = ""
            i += 1
            while size > 0:
                word += s[i]
                i += 1
                size -= 1
            strs.append(word)
        return strs

