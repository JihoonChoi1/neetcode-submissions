class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count1 = {}
        for i in s:
            char_count1[i] = char_count1.get(i, 0) + 1
        char_count2 = {}
        for i in t:
            char_count2[i] = char_count2.get(i, 0) + 1
        return char_count1 == char_count2
