class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int posLimit = Integer.MAX_VALUE / 10;
        int ret = 0;
        int t = x;
        while (t != 0) {
            int d = t % 10;
            if (ret > posLimit || (ret == posLimit && d > 7)) return false;
            ret = ret * 10 + d;
            t /= 10;
        }
        return ret == x;
    }
}
