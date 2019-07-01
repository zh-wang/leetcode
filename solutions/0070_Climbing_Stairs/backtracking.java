// Note that this will cause Time Limit Exceeded on leetcode
class Solution {
    public int climbStairs(int n) {
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        int ret = 0;
        ret += climbStairs(n - 2);
        ret += climbStairs(n - 1);
        return ret;
    }
}
