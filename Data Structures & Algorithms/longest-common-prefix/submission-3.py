class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = len(strs[0])
        for i in range(1, len(strs)):
            tmp = len(strs[i])
            if min > tmp:
                min = tmp;
        ret = "";
        numOfStrs = len(strs)
        for i in range(min):
            pre = strs[0][i]
            for j in range(1, numOfStrs):
                if pre != strs[j][i]:
                    return ret
            ret += pre    
        return ret
                

