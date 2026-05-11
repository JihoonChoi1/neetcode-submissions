class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = len(strs[0])
        for i in range(1, len(strs)):
            size = len(strs[i])
            if size < min:
                min = size
        word = strs[0]
        pre = ""
        for i in range(min):
            for s in strs:
                if word[i] != s[i]:
                    return pre
            pre += word[i]
        return pre
            
