class Solution {
    public int maxProduct(String[] words) {
        int ret = 0;
        int k = words.length;
        int[] b1 = new int[k]; // bit mask for high 13 bits
        int[] b2 = new int[k]; // bit mask for low 13 bits
        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < words[i].length(); ++j) {
                int d = words[i].charAt(j) - 'a'; // map char to each bit
                if (d >= 13) {
                    b2[i] |= (1 << (d - 13));
                } else {
                    b1[i] |= (1 << d);
                }
            }
        }
        for (int i = 0; i < k; ++i) {
            for (int j = i + 1; j < k; ++j) {
                if (hasNoCommonLetters(b1, b2, i, j)) {
                    ret = Math.max(ret, words[i].length() * words[j].length());
                }
            }
        }
        return ret;
    }

    private boolean hasNoCommonLetters(int[] b1, int[] b2, int i, int j) {
        return (b1[i] & b1[j]) == 0 && (b2[i] & b2[j]) == 0;
    }
}
