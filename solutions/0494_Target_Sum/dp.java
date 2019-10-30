class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int dp[][] = new int[21][2001]; // sum is [-1000, 1000], so adding 1000 to map it to [0, 2000]

        dp[0][1000] = 1; // initial state. 1000 can always be reached without any elements.

        for (int i = 1; i <= nums.length; ++i) {
            for (int j = 0; j < 2001; j++) {
                int a = j - nums[i-1]; // i-th element will be added
                // so dp[i][j] can be reached by adding nums[i] from dp[i-1][a]
                if (0 <= a && a < 2001 && dp[i-1][a] > 0) dp[i][j] += dp[i-1][a];
                a = j + nums[i-1]; // i-th element will be removed
                if (0 <= a && a < 2001 && dp[i-1][a] > 0) dp[i][j] += dp[i-1][a];
            }
        }
        return S > 1000 ? 0 : dp[nums.length][S + 1000];
    }
}
