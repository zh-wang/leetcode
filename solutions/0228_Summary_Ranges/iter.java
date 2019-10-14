class Solution {
    public List<String> summaryRanges(int[] nums) {
        // values with same 'nums[i] - i' are located in same range
        List<String> ret = new ArrayList<>();
        int start = 0;
        while (start < nums.length) {
            int end = endIndex(nums, start);
            if (start == end) {
                ret.add("" + (nums[start]));
            } else {
                ret.add("" + nums[start] + "->" + nums[end]);
            }
            start = end + 1;
        }
        return ret;
    }

    private int endIndex(int[] nums, int start) {
        int target = id(nums, start);
        start += 1;
        while (start < nums.length && id(nums, start) == target) {
            start += 1;
        }
        return start - 1;
    }

//     private int endIndex(int[] nums, int start) {
//         int target = id(nums, start);
//         int step = 1;
//         int end = start + step;
//         while (start + 1 < nums.length && id(nums, start + 1) == target) {
//             while (id(nums, start + step) == target) step *= 2;
//             start += step;
//         }
//         return start;
//     }

    private int id(int[] nums, int i) {
        return nums[i] - i;
    }
}
