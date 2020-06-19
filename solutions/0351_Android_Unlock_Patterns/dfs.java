// --Link--
// https://www.lintcode.com/problem/android-unlock-patterns/description

public class Solution {

    // 1 step movement
    private int[] dx = new int[] { -1, 0, 1 };
    private int[] dy = new int[] { -1, 0, 1 };

    // L-style movement
    private int[] di = new int[] { 1, 1, -1, -1, 2, 2, -2, -2 };
    private int[] dj = new int[] { 2, -2, 2, -2, 1, -1, 1, -1 };

    private int ret = 0;
    private int m = 0;
    private int n = 0;

    /**
     * @param m: an integer
     * @param n: an integer
     * @return: the total number of unlock patterns of the Android lock screen
     */
    public int numberOfPatterns(int m, int n) {
        // Write your code here
        this.m = m;
        this.n = n;
        boolean[][] visited = new boolean[3][3];
        for (int x = 0; x < 3; ++x) {
            for (int y = 0; y < 3; ++y) {
                this.dfs(x, y, 1, visited);
            }
        }
        return this.ret;
    }

    private void dfs(int x, int y, int depth, boolean visited[][]) {
        if (depth > n) {
            return;
        }
        if (depth >= m) {
            this.ret += 1;
        }
        visited[x][y] = true;
        for (int kx : dx) {
            for (int ky: dy) {
                int nx = kx + x;
                int ny = ky + y;
                if (nx == x && ny == y) continue;
                if (0 <= nx && nx < 3 && 0 <= ny && ny < 3) {
                    if (!visited[nx][ny]) {
                        dfs(nx, ny, depth + 1, visited);
                    } else {
                        int nnx = kx * 2 + x;
                        int nny = ky * 2 + y;
                        if (0 <= nnx && nnx < 3 && 0 <= nny && nny < 3) {
                            if (!visited[nnx][nny]) {
                                dfs(nnx, nny, depth + 1, visited);
                            }
                        }
                    }
                }
            }
        }
        for (int k = 0; k < 8; ++k) {
            int nx = x + di[k];
            int ny = y + dj[k];
            if (0 <= nx && nx < 3 && 0 <= ny && ny < 3 && !visited[nx][ny]) {
                this.dfs(nx, ny, depth + 1, visited);
            }
        }
        visited[x][y] = false;
    }
}
