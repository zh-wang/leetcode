class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int i = 1; i <= n; ++i) {
            if (i >= 2) {
                int last = Integer.valueOf(s.substring(i - 2, i));
                if (10 <= last && last <= 26) {
                    dp[i] += dp[i - 2];
                }
            }
            if (i >= 1) {
                int last = Integer.valueOf(s.substring(i - 1, i));
                if (1 <= last && last <= 9) {
                    dp[i] += dp[i - 1];
                }
            }
        }
        return dp[n];
    }
}
