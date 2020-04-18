class Solution {
    public int coinChange(int[] coins, int amount) {
        int maxVal = 0;
        for (int c : coins) maxVal = Math.max(c, maxVal);

        int dpsize = Math.min(maxVal, amount) + 1; // dp's size
        int[] dp = new int[dpsize];
        for (int i = 0; i < dp.length; ++i) dp[i] = Integer.MAX_VALUE; // init all slots to MAX
        dp[0] = 0; // first slot set to 0

        // loop i on dp array
        for (int i = 1; i <= amount; ++i) {
            int best = Integer.MAX_VALUE;
            for (int c : coins) {
                int index = (i - c + dp.length) % dp.length;
                if (i >= c && dp[index] != Integer.MAX_VALUE) {
                    best = Math.min(best, dp[index] + 1);
                }
            }
            dp[i % dp.length] = best;
        }
        return dp[amount % dp.length] == Integer.MAX_VALUE ? -1 : dp[amount % dp.length];
    }
}
