class Solution {
    public int lastRemaining(int n) {
        int l = 1;
        int r = n;
        int remain = n;
        int step = 0; // i-loop
        int span = 1; // span of a single remove
        while (l < r) {
            if (step % 2 == 0) { // odd loop, go left to right
                l += span;
                r = remain % 2 == 0 ? r : r - span;
            } else { // even loop, go right to left
                r -= span;
                l = remain % 2 == 0 ? l : l + span;
            }
            step += 1;
            remain -= (remain + 1) / 2;
            span *= 2;
        }
        return l;
    }
}
