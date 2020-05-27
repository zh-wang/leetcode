class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length <= 2) {
            return false;
        }
        int v1 = nums[0], v2 = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; ++i) {
            int v3 = nums[i];
            if (v2 < Integer.MAX_VALUE && v3 > v2) { // valid v3 is found
                return true;
            }
            if (v3 < v1) { // update v1
                v1 = v3;
            } else if (v1 < v3 && v3 < v2) { // update v2
                v2 = v3;
            }
        }
        return false;
    }
}
