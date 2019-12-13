// STAR

import java.util.TreeMap;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> cache = new TreeSet<>();
        int j = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (i - j > k) {
                cache.remove(Long.valueOf(nums[j++]));
            }
            Long l = cache.floor(Long.valueOf(nums[i]));
            if (l != null && nums[i] - l <= t) {
                return true;
            }
            Long r = cache.ceiling(Long.valueOf(nums[i]));
            if (r != null && r - nums[i] <= t) {
                return true;
            }
            cache.add(Long.valueOf(nums[i]));
        }
        return false;
    }
}
