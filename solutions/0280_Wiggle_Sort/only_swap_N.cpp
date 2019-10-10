// ⭐️

class Solution {
public:
    /*
     * @param nums: A list of integers
     * @return: nothing
     */
    void wiggleSort(vector<int> &nums) {
        // write your code here
        // x x x x x x x
        // ^ ^ ^
        // l i r
        // If we found an invalid pair l,i,r (Note that r maybe out of range)
        // we should decide swap left(l, i) or swap right(i, r)
        for (int i = 1; i < nums.size(); i += 2) {
            bool l = nums[i] >= nums[i-1];
            bool r = (i < nums.size() - 1) ? (nums[i] >= nums[i+1]) : true;
            // either swap left or right
            // r is false means i+1 in in range && nums[i+1] is larger than nums[i-1]
            if (!r && nums[i+1] > nums[i-1]) { // swap right
                int t = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = t;
            } else if (!l) { // otherwise, swap left
                int t = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = t;
            }
        }
    }
};
