class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.addup = [] # [m+1][n+1] 2d-array
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.addup += [[0] * (n + 1)]
        for i in range(m):
            l0 = [0] # add up for row i
            l1 = [0] # add up for matrix [0,0] to [i,j]
            for j in range(n):
                l0 += [matrix[i][j] + l0[-1]]
                l1 += [l0[-1] + self.addup[-1][j + 1]]
            self.addup += [l1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.addup[row2 + 1][col2 + 1] \
                - self.addup[row2 + 1][col1] \
                - self.addup[row1][col2 + 1] \
                + self.addup[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
