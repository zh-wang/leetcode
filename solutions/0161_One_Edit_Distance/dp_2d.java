// --Link--
// https://www.lintcode.com/problem/one-edit-distance/description

public class Solution {
    /**
     * @param s: a string
     * @param t: a string
     * @return: true if they are both one edit distance apart or false
     */
    public boolean isOneEditDistance(String s, String t) {
        // write your code here
        if (s == null || t == null) return false;
        int m = s.length() + 1, n = t.length() + 1;
        if (m == 0 && n == 0) return false;
        if (m == 0 && n == 1 || m == 1 && n == 0) return true;
        int[][] dp = new int[m][n];
        dp[0][0] = 0;
        for (int i = 1; i < m; ++i) dp[i][0] = i;
        for (int j = 1; j < n; ++j) dp[0][j] = j;
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (s.charAt(i-1) == t.charAt(j-1)) dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = Math.min(dp[i-1][j],
                                    Math.min(dp[i][j-1], dp[i-1][j-1])
                                    ) + 1;
            }
        }
        return dp[m-1][n-1] == 1;
    }
}
