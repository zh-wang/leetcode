// STAR

class Solution {
    public int findNumberOfLIS(int[] nums) {
        if (nums == null) {
            return 0;
        }
        if (nums.length <= 1) {
            return nums.length;
        }

        int best = 0;
        int dp[] = new int[nums.length]; // length of longest seq ends at nums[i]
        int paths[] = new int[nums.length]; // number of longest seqs end at nums[i]
        Arrays.fill(paths, 1);
        for (int i = 0; i < nums.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) { // found an increasing setup
                    if (dp[j] >= dp[i]) { // should update length
                        dp[i] = dp[j] + 1; // udpate length
                        paths[i] = paths[j]; // also update number of seqs
                    } else if (dp[j] + 1 == dp[i]) { // should only update number of seqs
                        paths[i] += paths[j];
                    }
                }
            }
            best = Math.max(best, dp[i]);
        }

        int ret = 0;
        for (int i = 0 ; i < nums.length; ++i) {
            if (dp[i] == best) {
                ret += paths[i];
            }
        }
        return ret;
    }
}
