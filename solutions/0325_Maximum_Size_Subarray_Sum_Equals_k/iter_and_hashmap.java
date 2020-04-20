public class Solution {
    /**
     * @param nums: an array
     * @param k: a target value
     * @return: the maximum length of a subarray that sums to k
     */
    public int maxSubArrayLen(int[] nums, int k) {
        // Write your code here
        if (nums.length == 0) {
            return 0;
        }
        int best = 0;
        Map<Integer, Integer> indexOfValue = new HashMap<>(); // <prefixSum, index>
        indexOfValue.put(0, 0); // initial value, prefixSum = 0 at index 0
        int prefixSum = 0;
        for (int i = 0; i < nums.length; ++i) {
            prefixSum += nums[i];
            if (indexOfValue.containsKey(prefixSum - k)) { // found
                // prefixSum - x = k ====> x = prefixSum - k
                int index = indexOfValue.get(prefixSum - k); // check that value exists
                best = Math.max(best, i - index + 1);
            }
            if (!indexOfValue.containsKey(prefixSum)) { // insert
                indexOfValue.put(prefixSum, i + 1); // +1 because added initial 0 at first
            }
        }
        return Math.max(best, 0);
    }
}
