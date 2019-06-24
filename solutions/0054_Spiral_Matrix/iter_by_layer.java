class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ret = new ArrayList<>();
        if (matrix.length == 0) {
            return ret;
        }
        int l = 0;
        int layer = (Math.min(matrix.length, matrix[0].length) + 1) / 2;
        while (l < layer) {
            int r1 = l;
            int r2 = matrix.length - 1 - l;
            int c1 = l;
            int c2 = matrix[0].length - 1 - l;
            // last layer is a horizontal line
            for (int c = c1; c <= c2; c++) ret.add(matrix[r1][c]);
            // last layer is a verticle line
            for (int r = r1 + 1; r <= r2; r++) ret.add(matrix[r][c2]);
            if (r1 < r2 && c1 < c2) {
                for (int c = c2 - 1; c > c1; c--) ret.add(matrix[r2][c]);
                for (int r = r2; r > r1; r--) ret.add(matrix[r][c1]);
            }
            l += 1;
        }
        return ret;
    }
}
