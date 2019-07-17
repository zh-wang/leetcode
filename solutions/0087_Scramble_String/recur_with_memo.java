class Solution {

    int[][][][] dp;

    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int[] count = new int[256];
        for (int i = 0; i < s1.length(); ++i) {
            count[s1.charAt(i)]++;
            count[s2.charAt(i)]--;
        }
        for (int i = 0; i < 256; ++i) {
            if (count[i] != 0) return false;
        }
        int m = s1.length();
        int n = s2.length();
        dp = new int[m][m][n][n];
        return isScrambleEqual(s1, s2, 0, m-1, 0, n-1);
    }

    private boolean isScrambleEqual(String s1, String s2, int l1, int r1, int l2, int r2) {
        // System.out.println(String.format("%d,%d  %d,%d", l1, r1, l2, r2));
        if (dp[l1][r1][l2][r2] != 0) return dp[l1][r1][l2][r2] > 0;
        if (l1 > r1 || l2 > r2) return false;
        if ( (r1 - l1) != (r2 - l2) ) return false;
        if (l1 == r1 || l2 == r2) {
            if (s1.charAt(l1) == s2.charAt(l2)) {
                dp[l1][r1][l2][r2] = 1;
                return true;
            } else {
                dp[l1][r1][l2][r2] = -1;
                return false;
            }
        }

        for (int f = 0; f < (r1-l1); ++f) {
            boolean ok1 = isScrambleEqual(s1, s2, l1, l1+f, l2, l2+f) &&
                isScrambleEqual(s1, s2, l1+f+1, r1, l2+f+1, r2);
            boolean ok2 = isScrambleEqual(s1, s2, l1, l1+f, r2-f, r2) &&
                isScrambleEqual(s1, s2, l1+f+1, r1, l2, r2-f-1);
            if (ok1 || ok2) {
                dp[l1][r1][l2][r2] = 1;
                return true;
            }
        }
        dp[l1][r1][l2][r2] = -1;
        return false;
    }
}
