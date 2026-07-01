class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:

        def backtrack(startIdx, root):
            cur = root

            for i in range(startIdx, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if backtrack(i+1, child):
                            return True
                    return False
                
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]

            return cur.endOfWord


        return backtrack(0, self.root)





        


