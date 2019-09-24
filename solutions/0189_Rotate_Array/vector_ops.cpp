class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() == 0) return;
        int steps = nums.size() - k % nums.size();
        for (int i = 0; i < steps; ++i) {
            nums.push_back(nums[i]);
        }
        for (int i = 0; i < steps; ++i) {
            nums.erase(nums.begin());
        }
    }
};
