class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = [(row, col) for row in range(9) for col in range(9) \
         for v in board[row][col] if v == '.']
        self.solvedBoard = [[]]
        self.solver(board, l, 0)
        board[:] = self.solvedBoard

    def solver(self, board, l, depth):
        # print(depth)
        if depth == len(l):
            self.solvedBoard = copy.deepcopy(board)
            return
        row, col = l[depth]
        bitmask = self.bitmask(board, row, col)
        for i in range(9):
            if (1 << i) & bitmask == 0:
                board[row][col] = str(i + 1)
                self.solver(board, l, depth + 1)
        board[row][col] = '.'

    def bitmask(self, board, row, col) -> List:
        bitmask = 0
        for i in range(9):
            if i != col and board[row][i] != '.':
                bitmask = bitmask | (1 << (int(board[row][i]) - 1))
            if i != row and board[i][col] != '.':
                bitmask = bitmask | (1 << (int(board[i][col]) - 1))
        for i in range(row//3*3, row//3*3 + 3):
            for j in range(col//3*3, col//3*3 + 3):
                if (i != row or j != col) and board[i][j] != '.':
                    bitmask = bitmask | (1 << (int(board[i][j]) - 1))
        return bitmask
