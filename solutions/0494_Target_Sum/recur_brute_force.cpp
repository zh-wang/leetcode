class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        if (nums.size() == 0) return 0;
        return recur(nums, 0, 0, S, 1);
    }

    int recur(vector<int>& nums, int i, int s, int S, int ways) {
        if (i >= nums.size()) {
            if (s == S) return ways;
            return 0;
        }
        return recur(nums, i+1, s+nums[i], S, ways) + recur(nums, i+1, s-nums[i], S, ways);
    }
};
