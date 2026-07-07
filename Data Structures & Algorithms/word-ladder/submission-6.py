class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        words = set(wordList)

        if endWord not in words:
            return 0

        n = len(beginWord)
        
        res = 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(n):
                    for c in range(ord('a'), ord('z')+1):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i+1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)

        return 0




        


