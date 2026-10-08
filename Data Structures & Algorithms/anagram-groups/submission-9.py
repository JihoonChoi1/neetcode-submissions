class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)].append(string)

        res = []
        for val in dic.values():
            res.append(val)
        return res

