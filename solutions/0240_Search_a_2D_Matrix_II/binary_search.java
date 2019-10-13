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
            // System.out.println("" + matrix[r1][c1]);
            if (matrix[r1][c1] == target) return true;
            else if (matrix[r1][c1] < target) {
                r1 = nextRow(matrix, target, r1+1, r2-1, c1);
            } else {
                c1 = nextCol(matrix, target, 0, c1-1, r1);
            }
        }
        return false;
    }

    // matrix[new_row][c1] >= target
    // basic binary search to find element >= target
    private int nextRow(int[][] matrix, int target,
                       int r1, int r2, int c1) {
        if (r1 >= r2) return r1;
        while (r1 < r2) {
            int m = (r1 + r2) / 2;
            if (matrix[m][c1] == target) return m;
            else if (matrix[m][c1] < target) {
                r1 = m + 1;
            } else {
                r2 = m;
            }
        }
        return r1;
    }

    // matrix[r1][next_col] <= target
    // modified binary search to find element <= target
    private int nextCol(int[][] matrix, int target,
                       int c1, int c2, int r1) {
        if (c2 <= 0) return c2;
        while (c1 < c2) {
            int m = (c1 + c2) / 2;
            if (matrix[r1][m] == target) return m;
            else if (matrix[r1][m] < target && matrix[r1][m+1] <= target) { // modified
                c1 = m + 1;
            } else {
                c2 = m;
            }
        }
        return c2;
    }
}
