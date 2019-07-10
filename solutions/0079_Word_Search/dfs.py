class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.di, self.dj = [0, 1, 0, -1], [-1, 0, 1, 0]
        self.m, self.n = len(board), len(board[0])
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.find(board, word, 0, i, j, visited):
                    return True
        return False

    def find(self, board, word, word_index, i, j, visited):
        if word_index + 1 >= len(word):
            return True
        visited[i][j] = True
        ret = False
        for k in range(4):
            ki, kj = i + self.di[k], j + self.dj[k]
            if 0 <= ki < self.m and 0 <= kj < self.n and not visited[ki][kj] and board[ki][kj] == word[word_index + 1]:
                ret = ret or self.find(board, word, word_index+1, ki, kj, visited)
        visited[i][j] = False
        return ret
