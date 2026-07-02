class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        trie = Trie()

        rowLen = len(board)
        colLen = len(board[0])

        visited = [[0] * len(board[0]) for _ in range(len(board))]

        for word in words:
            trie.addWord(word)

        def dfs(row, col, cur, node):
            if not (0 <= row < rowLen and 0 <= col < colLen):
                return
            c = board[row][col]
            if c not in node.children or visited[row][col]:
                return

            nxt = node.children[c]
            if nxt.refs == 0:
                return
            cur.append(c)
            if nxt.isWord:
                res.append("".join(cur))
                nxt.isWord = False
                nxt.refs -= 1
                if nxt.refs == 0:
                    del node.children[c]
                    cur.pop()
                    return
                
            visited[row][col] = True
            dfs(row-1, col, cur, nxt)
            dfs(row+1, col, cur, nxt)
            dfs(row, col-1, cur, nxt)
            dfs(row, col+1, cur, nxt)
            visited[row][col] = False
            cur.pop()

        for rowIdx in range(rowLen):
            for colIdx in range(colLen):
                dfs(rowIdx, colIdx, [], trie.root)

        return res















