public class Solution {
    /**
     * @param nums: a sorted array
     * @param a:
     * @param b:
     * @param c:
     * @return: a sorted array
     */
    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {
        // Write your code here
        int[] ret = new int[nums.length];
        if (a == 0) {
            for (int i = 0; i < nums.length; ++i) ret[i] = b * nums[i] + c;
            if (b < 0) reverse(ret);
            return ret;
        }
        for (int i = 0; i < nums.length; ++i) {
            nums[i] = calc(nums[i], a, b, c);
        }
        int l = 0, r = nums.length - 1;
        if (a > 0) {
            int i = nums.length - 1;
            while (l < r) {
                if (nums[l] > nums[r]) ret[i--] = nums[l++];
                else ret[i--] = nums[r--];
            }
            ret[i] = nums[l];
        } else {
            int i = 0;
            while (l < r) {
                if (nums[l] < nums[r]) ret[i++] = nums[l++];
                else ret[i++] = nums[r--];
            }
            ret[i] = nums[l];
        }
        return ret;
    }

    private void reverse(int[] arr) {
        for (int i = 0; i < arr.length / 2; ++i) {
            int temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
    }

    private int calc(int v, int a, int b, int c) {
        return a * v * v + b * v + c;
    }
}
