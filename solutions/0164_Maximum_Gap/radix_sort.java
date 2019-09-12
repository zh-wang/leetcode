class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length <= 1) return 0;
        radixSort(nums);
        int best = 0;
        for (int i = 0; i < nums.length - 1; ++i) {
            best = Math.max(best, nums[i+1] - nums[i]);
        }
        return best;
    }

    private void radixSort(int[] nums) {
        int[] keys = new int[nums.length];
        int m = 0, n = nums.length;
        int step = 1;
        for (int i = 0; i < nums.length; ++i) {
            m = Math.max(m, nums[i]);
        }
        while (step <= m) {
            for (int i = 0; i < n; ++i) keys[i] = (nums[i] / step) % 10;
            countSort(keys, nums);
            step *= 10;
        }
    }

    private void countSort(int[] keys, int[] nums) {
        int n = keys.length;
        int[] C = new int[11];
        Arrays.fill(C, 0);
        int[] B = new int[n];
        for (int a : keys) C[a] += 1;
        for (int i = 1; i < 11; ++i) C[i] = C[i] + C[i-1];
        for (int i = n-1; i >= 0; --i) {
            B[C[keys[i]]] = nums[i];
            C[keys[i]] -= 1;
        }
        for (int i = 0; i < n; ++i) nums[i] = B[i];
    }
}
