class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int e = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[e--] = nums1[i--];
            } else {
                nums1[e--] = nums2[j--];
            }
        }
        if (j >= 0) {
            for (int k = 0; k <= j; ++k) nums1[k] = nums2[k];
        }
    }
}
