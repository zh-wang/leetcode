class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        // special case when nums contains only one neg element
        if (nums.length == 1 && nums[0] < 0) {
            return nums[0];
        }
        int best = 0;
        int pos = 0, neg = 0; // positive product, negative product until i
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 0) { // reset pos & neg when encounter 0
                best = Math.max(best, pos);
                pos = neg = 0;
            } else if (nums[i] > 0) { // update both when encounter a pos elem
                if (pos == 0) pos = nums[i];
                else pos *= nums[i];
                neg *= nums[i];
            } else { // when encounter a neg elem, we have 4 cases
                best = Math.max(best, pos); // *** update best, cause pos may be lost or changed in case 3 and case 4
                if (pos == 0 && neg == 0) { // case 1, both of them are 0
                    neg = nums[i]; // only update neg
                } else if (pos == 0) { // case 2
                    pos = neg * nums[i]; // update pos
                    neg = nums[i]; // init neg
                } else if (neg == 0) { // case 3
                    neg = pos * nums[i]; // update neg
                    pos = 0; // reset pos
                } else { // case 4
                    int new_pos = neg * nums[i]; // update both
                    int new_neg = pos * nums[i];
                    pos = new_pos;
                    neg = new_neg;
                }
            }
        }
        best = Math.max(best, pos);
        return best;
    }
}
