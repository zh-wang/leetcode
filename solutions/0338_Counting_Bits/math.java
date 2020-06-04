class Solution {
    public int[] countBits(int num) {
        int[] ret = new int[num + 1];
        if (num == 0) {
            ret[0] = 0;
            return ret;
        }
        // let f(n) to be the number of 1's in n's binary representation
        // f(n) = f(n / 2) + 1    if n % 2 == 1
        //      = f(n / 2)        otherwise
        for (int i = 1; i < ret.length; ++i) {
            ret[i] = ret[i / 2] + (i % 2);
        }
        return ret;
    }
}
