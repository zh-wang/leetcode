class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return s;
        int n = s.length();
        int a = 0, b = 0;
        for (int i = 0; i < n; ++i) {
            int size1 = sizeOfPanliWithCenter(i, i, s); // A: pattern like 'aba', centered as 'b'
            int size2 = sizeOfPanliWithCenter(i, i+1, s); // B: pattern like 'abba', centerd as 'bb'
            int size = Math.max(size1, size2);
            if (size > b - a) {
                // tricky part
                // A: size is odd, move distance is (size - 1) / 2. e.g. if size == 3 we move 1 to the left
                // B: size is even, move distance is also (size - 2) / 2. But the value is same as (size - 1) / 2
                a = i - (size - 1) / 2;
                // A: same
                // B: because we start from i, so we move 1 more slot than above. (size - 2) / 2 + 1 => size / 2
                b = i + size / 2;
            }
        }
        return s.substring(a, b + 1);
    }

    private int sizeOfPanliWithCenter(int i, int j, String s) {
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            --i;
            ++j;
        }
        return j - i - 1; // (j - 1) - (i + 1) + 1
                          // r index   l index
    }
}
