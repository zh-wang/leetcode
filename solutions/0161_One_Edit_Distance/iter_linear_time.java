// ⭐️  --Link--
// https://www.lintcode.com/problem/one-edit-distance/description

public class Solution {
    /**
     * @param s: a string
     * @param t: a string
     * @return: true if they are both one edit distance apart or false
     */
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();
        if (m == n) { // count diff in each char, if s & t are same length
            int diff = 0;
            for (int i = 0; i < m; ++i) {
                diff += s.charAt(i) == t.charAt(i) ? 0 : 1;
                if (diff > 1) return false;
            }
            return diff == 1;
        }
        if (Math.abs(m - n) == 1) { // check both sides, if s & t's length diffs in 1
            int i = 0, j = 0;
            int k = Math.min(m, n);
            while (i < k && s.charAt(i) == t.charAt(i)) ++i;
            while (j < k && s.charAt(m - 1 - j) == t.charAt(n - 1 - j)) ++j;
            return i + j == k;
        }
        return false;
    }
}
