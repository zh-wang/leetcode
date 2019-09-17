class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        int minSum = minPartSum(dungeon, m, n);
        // binary search [l, r] to get the answer
        int l = 1;
        int r = minSum >= 0 ? 1 : Math.abs(minSum) + 1;
        while (l < r) {
            // System.out.println("" + l + ", " + r);
            int life = (l + r) / 2;
            if (canReach(dungeon, life, m, n)) {
                r = life;
            } else {
                l = life + 1;
            }
        }
        return l;
    }

    public int minPartSum(int[][] dungeon, int m, int n) {
        int dp[] = new int[n];
        int minSum = dungeon[0][0];
        dp[0] = dungeon[0][0];
        for (int j = 1; j < n; ++j) {
            dp[j] = dp[j-1] + dungeon[0][j];
            minSum = Math.min(minSum, dp[j]);
        }
        for (int i = 1; i < m; ++i) {
            dp[0] = dp[0] + dungeon[i][0];
            minSum = Math.min(minSum, dp[0]);
            for (int j = 1; j < n; ++j) {
                dp[j] = Math.min(dp[j-1], dp[j]) + dungeon[i][j];
                minSum = Math.min(minSum, dp[j]);
            }
        }
        return minSum;
    }

    public boolean canReach(int[][] dungeon, int life, int m, int n) {
        int dp[] = new int[n];
        dp[0] = life + dungeon[0][0];
        if (dp[0] <= 0) return false; // life cannot zero or negative
        for (int j = 1; j < n; ++j) {
            if (dp[j-1] > 0) { // only update dp when life is positive
                dp[j] = dp[j-1] + dungeon[0][j];
            }
        }
        for (int i = 1; i < m; ++i) {
            if (dp[0] > 0) {
                dp[0] = dp[0] + dungeon[i][0];
            }
            for (int j = 1; j < n; ++j) {
                if (dp[j-1] > 0 && dp[j] > 0) {
                    dp[j] = Math.max(dp[j-1], dp[j]) + dungeon[i][j];
                } else if (dp[j-1] > 0) {
                    dp[j] = dp[j-1] + dungeon[i][j];
                } else if (dp[j] > 0) {
                    dp[j] = dp[j] + dungeon[i][j];
                }
            }
        }
        return dp[n-1] > 0;
    }
}
