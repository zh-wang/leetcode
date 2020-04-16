// This will cause Memory Limit Exceeded on OJ

class Solution {
    public int bulbSwitch(int n) {
        // The first bulb will always be on.
        if (n <= 1) {
            return n;
        }
        int[] tb = new int[n + 1];
        for (int i = 2; i <= n; ++i) {
            int k = i;
            while (k <= n) {
                tb[k] += 1;
                k += i;
            }
        }
        int ret = 1;
        for (int i = 2; i <= n; ++i) {
            if ((tb[i] & 1) == 0) ret += 1;
        }
        return ret;
    }
}
