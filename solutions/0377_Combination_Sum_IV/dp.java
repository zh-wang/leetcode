class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (target == 0) {
            return 1;
        }
        int[] dp = new int[target + 1];
        dp[0] = 1;
        Arrays.sort(nums);
        for (int i = 1; i <= target; ++i) {
            int cnt = 0;
            for (int v : nums) {
                if (i - v >= 0 && dp[i - v] >= 0) cnt += dp[i - v];
            }
            dp[i] = cnt;
        }
        return dp[target];
    }
}
