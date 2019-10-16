// --Link--
// https://www.lintcode.com/problem/3sum-smaller/description

public class Solution {
    /**
     * @param nums:  an array of n integers
     * @param target: a target
     * @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
     */
    public int threeSumSmaller(int[] nums, int target) {
        // Write your code here
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int ret = 0, n = nums.length;
        for (int i = 1; i < n - 1; ++i) {
            int l = 0;
            int r = n - 1;
            while (l < i-1 || i+1 < r) {
                int total = nums[l] + nums[i] + nums[r];
                if (total < target) { // we should find a larger nums[l]
                    ret += (r - i);
                    if (l < i-1) ++l;
                    else break;
                } else { // we should a smaller nums[r]
                    if (i+1 < r) --r;
                    else break;
                }
            }
            if (l+1 == i && i+1 == r && nums[l] + nums[i] + nums[r] < target) ++ret;
        }
        return ret;
    }
}
