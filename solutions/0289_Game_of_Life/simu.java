class Solution {
    public void gameOfLife(int[][] board) {
        int[] di = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dj = {-1, 0, 1, -1, 1, -1, 0, 1};
        int n = board.length;
        if (n == 0) return;
        int m = board[0].length;
        if (m == 0) return;

        int[][] nextBoard = new int[n][m];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (board[i][j] == 1) {
                    int liveCnt = 0;
                    for (int k = 0; k < di.length; ++k) {
                        if (isValidPos(i + di[k], j + dj[k], n, m) && board[i + di[k]][j + dj[k]] == 1) liveCnt++;
                    }
                    if (2 <= liveCnt && liveCnt <= 3) nextBoard[i][j] = 1;
                } else {
                    int liveCnt = 0;
                    for (int k = 0; k < di.length; ++k) {
                        if (isValidPos(i + di[k], j + dj[k], n, m) && board[i + di[k]][j + dj[k]] == 1) liveCnt++;
                    }
                    if (liveCnt == 3) nextBoard[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                board[i][j] = nextBoard[i][j];
            }
        }
    }

    private boolean isValidPos(int i, int j, int n, int m) {
        if (0 <= i && i < n && 0 <= j && j < m) return true;
        return false;
    }
}
