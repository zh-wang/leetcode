// ⭐️

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null) return false;
        int r2 = matrix.length;
        if (r2 == 0) return false;
        int c2 = matrix[0].length;
        if (c2 == 0) return false;
        if (target < matrix[0][0] || target > matrix[r2-1][c2-1]) return false;
        int r1 = 0, c1 = c2 - 1;
        while (r1 < r2 && c1 >= 0) {
            if (matrix[r1][c1] == target) return true;
            else if (matrix[r1][c1] < target) {
                r1 += 1;
            } else {
                c1 -= 1;
            }
        }
        return false;
    }
}
