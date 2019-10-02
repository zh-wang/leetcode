class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ret = 0;
        while (n > 0) {
            ret += (n & 1) > 0 ? 1 : 0;
            n >>= 1;
        }
        return ret;
    }
};
