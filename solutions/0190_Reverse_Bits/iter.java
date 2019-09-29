public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int count = 0;
        int ret = 0;
        while (count < 32) {
            int v = n & 1;
            n >>= 1;
            ret = (ret << 1) + v;
            ++count;
        }
        return ret;
    }
}
