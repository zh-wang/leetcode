class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        for (int i = 1; i <= amount; ++i) {
            dp[i] = -1;
            int best = Integer.MAX_VALUE;
            for (int c : coins) {
                if (i >= c && dp[i - c] >= 0) {
                    best = Math.min(best, dp[i - c] + 1);
                }
            }
            if (best < Integer.MAX_VALUE) {
                dp[i] = best;
            }
        }
        return dp[dp.length - 1];
    }
}
