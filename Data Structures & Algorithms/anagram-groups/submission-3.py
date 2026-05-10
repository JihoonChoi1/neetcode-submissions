class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in container:
                container[key] = []
            container[key].append(strs[i])
        return list(container.values())
