class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            tmp = [0] * 26
            for c in string:
                tmp[ord(c) - ord('a')] += 1
            groups[tuple(tmp)].append(string)
        return list(groups.values())
            
            