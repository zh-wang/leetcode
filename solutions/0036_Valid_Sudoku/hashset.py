class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        entries = sum( \
                    ([(row, v), (v, col), (row//3, col//3, v)] \
                    for row in range(9) \
                    for col in range(9) \
                    for v in board[row][col] if v != '.'), \
                    [])
        return len(entries) == len(set(entries))
