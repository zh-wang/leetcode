// ⭐️

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 3 => 1, 1
        // 4 => 1, 2
        // 5 => 2, 2
        // k => (k + 1) / 2 - 1, (k + 2) / 2 - 1
        int m = nums1.length, n = nums2.length;
        // why -1 is not here?
        // Because we need k starts from 1, so k - k/2 works when k >= 2
        // If k starts from 0, then k - k/2 stops at k == 1
        int l = (m + n + 1) / 2;
        int r = (m + n + 2) / 2;
        int lv = KthInBoth(nums1, 0, nums2, 0, l);
        int rv = KthInBoth(nums1, 0, nums2, 0, r);
        return (lv + rv) / 2.0f;
    }

    private int KthInBoth(int[] nums1, int s1, int[] nums2, int s2, int k) {
        if (s1 >= nums1.length) return nums2[s2 + k - 1];
        if (s2 >= nums2.length) return nums1[s1 + k - 1];

        if (k == 1) return Math.min(nums1[s1], nums2[s2]);

        int m1 = s1 + k/2 - 1 >= nums1.length ? Integer.MAX_VALUE : nums1[s1 + k/2 - 1];
        int m2 = s2 + k/2 - 1 >= nums2.length ? Integer.MAX_VALUE : nums2[s2 + k/2 - 1];
        if (m1 < m2) {
            return KthInBoth(nums1, s1 + k/2, nums2, s2,       k - k/2);
        } else {
            return KthInBoth(nums1, s1,       nums2, s2 + k/2, k - k/2);
        }
    }
}
