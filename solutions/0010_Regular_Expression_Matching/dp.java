class Solution {
    public boolean isMatch(String s, String p) {
        int n = s.length() + 1;
        int m = p.length() + 1;
        boolean[][] dp = new boolean[n][m];
        dp[0][0] = true; // both s & p are empty
        for (int j = 1; j < m; ++j) {
            if (p.charAt(j - 1) == '*') dp[0][j] = dp[0][j - 2]; // '*' can match an empty s
        }
        for (int i = 1; i < n; ++i) {
            for (int j = 1; j < m; ++j) {
                char sc = s.charAt(i - 1);
                char pc = p.charAt(j - 1);
                if (pc == '*' && j - 2 >= 0) {
                    if (p.charAt(j - 2) == sc || p.charAt(j - 2) == '.') {
                        dp[i][j] = dp[i][j - 2] | dp[i][j - 1] | dp[i - 1][j];
                    } else {
                        dp[i][j] = dp[i][j - 2];
                    }
                }
                if (sc == pc || pc == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        return dp[n - 1][m - 1];
    }
}
