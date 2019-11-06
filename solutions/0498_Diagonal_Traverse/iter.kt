class Solution {
    fun findDiagonalOrder(matrix: Array<IntArray>): IntArray {
        if (matrix.isEmpty() || matrix[0].isEmpty()) {
            return IntArray(0)
        }
        val m = matrix.size - 1
        val n = matrix[0].size - 1
        var r = 0
        var c = 0
        var ret = IntArray(0)
        for (l in 0..m + n + 1) {
            if (l % 2 == 0) {
                val steps = Math.min(r, n - c)
                for (s in 0..steps) {
                    ret += matrix[r - s][c + s]
                }
                r -= steps
                c += steps
                if (c < n) {
                    c += 1
                } else {
                    r += 1
                }
            } else {
                val steps = Math.min(m - r, c)
                for (s in 0..steps) {
                    ret += matrix[r + s][c - s]
                }
                r += steps
                c -= steps
                if (r < m) {
                    r += 1
                } else {
                    c += 1
                }
            }
        }
        return ret
    }
}
