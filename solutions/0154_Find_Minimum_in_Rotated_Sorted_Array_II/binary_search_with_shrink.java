class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 0) return 0;
        int l = 0, r = nums.length - 1;
        while (l < r) {
            // shrink left side until nums[l] != nums[r]
            while (l < r && nums[l] == nums[r]) {
                l += 1;
            }
            int m = (l + r) / 2;
            if (nums[l] > nums[m]) { // pivot in first half
                r = m; // this still holds when nums[m] == nums[r]
            } else if (nums[m] > nums[r]) { // pivot in second half
                l = m + 1; // this still holds when nums[l] == nums[m]
            } else { // sorted
                return nums[l];
            }
        }
        return nums[l];
    }
}
