class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length <= 1) return 0;
        Arrays.sort(nums);
        int best = 0;
        for (int i = 0; i < nums.length - 1; ++i) {
            best = Math.max(best, nums[i+1] - nums[i]);
        }
        return best;
    }
}
