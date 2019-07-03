class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowIsZero, firstColIsZero = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                # flip [i,j] to [0,i] and [j,0]
                if matrix[i][j] == 0:
                    if i > 0 and j > 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                    else:
                        if i == 0:
                            firstRowIsZero = True
                        if j == 0:
                            firstColIsZero = True
        # fill matrix[1,1] to [m, n] with zero if first row/col is set
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # fill first row
        if firstRowIsZero:
            for j in range(n):
                matrix[0][j] = 0
        # fill first col
        if firstColIsZero:
            for i in range(m):
                matrix[i][0] = 0
