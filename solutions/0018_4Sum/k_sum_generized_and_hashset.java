class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, target, 0, 4);
    }

    private List<List<Integer>> kSum(int[] nums, int target, int start, int k) {
        List<List<Integer>> ret = new ArrayList<>();
        int n = nums.length;
        if (start >= nums.length ||
            nums[start] * k > target ||
            target > nums[n - 1] * k) {
            return ret;
        }
        if (k == 2) {
            return twoSum(nums, target, start);
        }
        for (int i = start; i < n; ++i) {
            if (i == start || nums[i - 1] != nums[i]) {
                for (var set : kSum(nums, target - nums[i], i + 1, k - 1)) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.addAll(set);
                    ret.add(temp);
                }
            }
        }
        return ret;
    }

    private List<List<Integer>> twoSum(int[] nums, int target, int start) {
        List<List<Integer>> ret = new ArrayList<>();
        int n = nums.length;
        Set<Integer> s = new HashSet<>();
        for (int i = start; i < n; ++i) {
            // initial        || skip same value (which is nums[i])
            if (ret.isEmpty() || ret.get(ret.size() - 1).get(1) != nums[i]) {
                if (s.contains(target - nums[i])) {
                    ret.add(Arrays.asList(target - nums[i], nums[i]));
                }
            }
            s.add(nums[i]);
        }
        return ret;
    }
}
