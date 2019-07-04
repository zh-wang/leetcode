class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        s, t = 0, m * n - 1
        while s < t:
            mid = (s + t) // 2
            if matrix[mid//n][mid%n] >= target:
                t = mid
            else:
                s = mid + 1
        return matrix[s//n][s%n] == target
