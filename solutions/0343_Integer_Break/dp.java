class Solution {
    public int integerBreak(int n) {
        if (n == 1) return 1;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 1; i <= n; ++i) {
            int best = 0;
            for (int j = 1; j <= i / 2; ++j) {
                best = Math.max(best,
                                Math.max(dp[j], j) * Math.max(i - j, dp[i - j]));
            }
            dp[i] = best;
        }
        return dp[n];
    }
}
