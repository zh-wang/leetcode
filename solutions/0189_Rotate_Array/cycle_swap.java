class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        int start = 0;
        while (count < nums.length) {
            count += cycleSwap(start, nums, k);
            ++start;
        }
    }

    private int cycleSwap(int start, int[] nums, int k) {
        int count = 0;
        int cur = start; // current index
        int out = nums[cur]; // keep the value swap out
        int next = (cur + k) % nums.length; // next index
        while (start != next) {
            int temp = nums[next]; // swap nums[next] with out
            nums[next] = out;
            out = temp;
            cur = next; // calc indice for next loop
            next = (cur + k) % nums.length;
            ++count;
        }
        nums[next] = out; // swap the last index before exiting
        ++count;
        return count;
    }
}
