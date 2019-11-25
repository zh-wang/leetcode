from typing import *

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not len(board) or not len(board[0]):
            return []
        m, n = len(board), len(board[0])
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        self.maxLength = 0
        self.ds = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        trie = Trie()
        for w in words:
            trie.insert(w)
            self.maxLength = max(self.maxLength, len(w))
        self.ret = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root:
                    self.visited[i][j] = True
                    self.findWord(board, trie.root[board[i][j]], i, j, [board[i][j]], 1)
                    self.visited[i][j] = False
        return list(self.ret)

    def findWord(self, board, node, i, j, foundWord, depth):
        if not node or depth > self.maxLength:
            return
        if '$' in node:
            self.ret.add(''.join(foundWord))
        for d in self.ds:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not self.visited[ni][nj] and board[ni][nj] in node:
                self.visited[ni][nj] = True
                self.findWord(board, node[board[ni][nj]], ni, nj, foundWord + [board[ni][nj]], depth + 1)
                self.visited[ni][nj] = False

class Trie():
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None

# x = Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
# x = Solution().findWords([["a","b"]], ["ba"])
# print(x)
