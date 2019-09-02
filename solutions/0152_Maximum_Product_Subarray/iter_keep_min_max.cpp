class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int pmax, pmin, best;
        pmax = pmin = best = nums[0]; // max product, min product ending at i
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] >= 0) { // this step can reset pmax & pmin when encounter 0
                pmax = max(nums[i], pmax * nums[i]);
                pmin = min(nums[i], pmin * nums[i]);
            } else {
                int temp = pmax; // exchange pmax & pmin when encounter neg elem
                pmax = max(nums[i], pmin * nums[i]);
                pmin = min(nums[i], temp * nums[i]);
            }
            best = max(best, pmax);
        }
        return best;
    }
};
