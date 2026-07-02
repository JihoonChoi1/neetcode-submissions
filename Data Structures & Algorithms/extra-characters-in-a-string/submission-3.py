class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res = 50
        n = len(s)
        trie = Trie()
        dp = [0] * (n + 1)
        dp[n] = 0

        for word in dictionary:
            trie.addWord(word)

        for i in range(n-1,-1,-1):
            dp[i] = 1 + dp[i+1]
            cur = trie.root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    dp[i] = min(dp[i], dp[j+1])


        return dp[0]

                

