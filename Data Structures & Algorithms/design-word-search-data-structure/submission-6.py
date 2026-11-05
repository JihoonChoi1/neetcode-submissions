class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(startIdx, node):

            for i in range(startIdx, len(word)):
                if word[i] == '.':
                    for curr in node.children.values():
                        if dfs(i + 1, curr):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            
            return node.endOfWord

        return dfs(0, self.root)
                    


                

            
