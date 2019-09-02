class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int pos, neg, best;
        pos = neg = best = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] >= 0) { // this step can reset pos & neg when encounter 0
                pos = max(nums[i], pos * nums[i]);
                neg = min(nums[i], neg * nums[i]);
            } else {
                int temp = pos; // exchange pos & neg when encounter neg elem
                pos = max(nums[i], neg * nums[i]);
                neg = min(nums[i], temp * nums[i]);
            }
            best = max(best, pos);
        }
        return best;
    }
};
