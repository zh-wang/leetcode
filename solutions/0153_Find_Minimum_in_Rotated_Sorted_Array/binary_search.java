class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 0) return 0;
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int m = (l + r) / 2;
            if (nums[l] > nums[m]) { // pivot in first half
                r = m;
            } else if (nums[r] < nums[m]) { // pivot in second half
                l = m + 1;
            } else { // sorted!
                return nums[l];
            }
        }
        return nums[l];
    }
}
