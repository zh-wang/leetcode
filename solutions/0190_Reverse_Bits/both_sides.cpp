class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t h = 1 << 31;
        uint32_t l = 1;
        while (h > l) {
            uint32_t v1 = h & n;
            uint32_t v2 = l & n;
            if (v1 > 0 && v2 == 0) {
                n = n - h + l;
            } else if (v1 == 0 && v2 > 0) {
                n = n - l + h;
            }
            h >>= 1;
            l <<= 1;
        }
        return n;
    }
};
