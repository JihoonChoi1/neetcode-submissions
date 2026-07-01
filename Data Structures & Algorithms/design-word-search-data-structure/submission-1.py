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
        node = self.root

        def backtrack(startIdx, node):

            for i in range(startIdx, len(word)):
                if word[i] == ".":
                    for child in node.children.values():
                        if backtrack(i+1, child):
                            return True
                    return False
                
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]

            return node.endOfWord


        return backtrack(0, self.root)





        


