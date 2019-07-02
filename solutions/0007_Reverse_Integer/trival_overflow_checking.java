class Solution {
    public int reverse(int x) {
        int ret = 0;
        int posLimit = Integer.MAX_VALUE / 10;
        int negLimit = Integer.MIN_VALUE / 10;
        while (x != 0) {
            int d = x % 10;
            x /= 10;

            if (ret > posLimit || (ret == posLimit && d > 7)) return 0;
            if (ret < negLimit || (ret == negLimit && d < -8)) return 0;

            ret = ret * 10 + d;
        }
        return ret;
    }
}
