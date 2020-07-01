class Solution {
    public int longestValidParentheses(String s) {
        if (s.length() <= 1) {
            return 0;
        }
        int best = 0;
        int[] dp = new int[s.length()];
        for (int i = 1; i < s.length(); ++i) {
            // dp[i] = 0                        if s[i] == '('
            //       = dp[i-2] + 2              if s[i] == ')' and s[i-1] == '('
            //                                  (let pi = i - dp[i-1] - 1)
            //       = dp[i-1] + dp[pi-1] + 2    if s[i] == ')' and s[i-1] == ')'
            //                                      and s[pi] == '('
            if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') { // found '()'
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                } else { // str ends with '))'   ()((xxxxxx))
                    //                             ^        ^
                    // s:                          pi       i
                    //                            ^
                    // dp:                      dp[pi-1]
                    int pi = i - dp[i - 1] - 1;
                    if (pi >= 0 && s.charAt(pi) == '(') { // if that is '('
                        // we extend the length
                        dp[i] = dp[i - 1] + (pi > 0 ? dp[pi - 1] : 0) + 2;
                    }
                }
            }
            best = Math.max(best, dp[i]);
        }
        return best;
    }
}
