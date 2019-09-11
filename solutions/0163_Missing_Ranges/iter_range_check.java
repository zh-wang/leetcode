// --Link--
// https://www.lintcode.com/problem/missing-ranges/description
public class Solution {
    /*
     * @param nums: a sorted integer array
     * @param lower: An integer
     * @param upper: An integer
     * @return: a list of its missing ranges
     */
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        // write your code here
        List<String> ret = new ArrayList<>();
        if (lower > upper) return ret;
        if (nums.length == 0) {
            ret.add(str(lower, upper));
            return ret;
        }
        int l = 0, r = nums.length - 1;
        while (l < nums.length && nums[l] < lower) ++l;
        while (r >= 0 && nums[r] > upper) --r;
        if (l > r) {
            ret.add(str(lower, upper));
        } else if (l == r) {
            if (lower < nums[l]) ret.add(str(lower, nums[l]-1));
            if (upper > nums[l]) ret.add(str(nums[l]+1, upper));
        } else {
            if (lower < nums[l]) ret.add(str(lower, nums[l]-1));
            for (int i = l; i <= r - 1; ++i) {
                // left value cannot be Integer.MAX_VALUE
                // right value cannot be Integer.MIN_VALUE
                if (nums[i] != Integer.MAX_VALUE && nums[i+1] != Integer.MIN_VALUE && nums[i]+1 <= nums[i+1]-1) {
                    ret.add(str(nums[i]+1, nums[i+1]-1));
                }
            }
            if (upper > nums[r]) ret.add(str(nums[r]+1, upper));
        }
        return ret;
    }

    private String str(int l, int r) {
        return l < r ? "" + l + "->" + r : "" + l;
    }
}
