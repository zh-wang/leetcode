class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) {
            return true;
        }
        int best_reach = 0;
        int s = 0;
        while (s <= best_reach && best_reach < nums.length) {
            best_reach = Math.max(best_reach, s + nums[s]);
            ++s;
        }
        return best_reach >= nums.length - 1;
    }
}
