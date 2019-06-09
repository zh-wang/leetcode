class Solution {
    public int longestValidParentheses(String s) {
        int best = 0;
        int[] dp = new int[s.length() + 1]; // ith in dp => (i-1)th in s
        dp[0] = 0;
        for (int i = 1; i < s.length() + 1; ++i) {
            if (s.charAt(i - 1) == '(') { // str ends with '(' is always not satisfied
                dp[i] = 0;
            } else { // str ends with ')'
                if (i - 1 - 1 >= 0 && s.charAt(i - 1 - 1) == '(') { // ends with '()'
                    dp[i] = dp[i - 2] + 2;
                } else { // str ends with '))'   ()((xxxxxx))
                    //                             ^        ^
                    // s:                          pi      i-1
                    //                            ^
                    // dp:                      dp[pi]
                    int pi = i - 1 - dp[i - 1] - 1;
                    if (pi >= 0 && s.charAt(pi) == '(') { // if that is '('
                        // we can extend the length
                        dp[i] = dp[i - 1] + dp[pi] + 2;
                    }
                }
            }
            best = Math.max(best, dp[i]);
        }
        return best;
    }
}
