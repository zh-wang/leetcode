class Solution {

    private Map<String, Boolean> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int m = s1.length();
        int n = s2.length();
        int[] count = new int[26];

        String merge01 = s1 + s2;
        if (memo.containsKey(merge01)) return memo.get(merge01);
        String merge02 = s2 + s1;
        if (memo.containsKey(merge02)) return memo.get(merge02);

        if (s1.equals(s2)) {
            memo.put(merge01, true);
            return true;
        }

        for (int i = 0; i < m; ++i) {
            ++count[s1.charAt(i) - 'a'];
            --count[s2.charAt(i) - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (count[i] != 0) {
                memo.put(merge01, false);
                return false;
            }
        }

        for (int i = 1; i < m; ++i) {
            boolean ok01 = isScramble(s1.substring(0, i), s2.substring(0, i)) &&
                isScramble(s1.substring(i), s2.substring(i));
            boolean ok02 = isScramble(s1.substring(0, i), s2.substring(m - i)) &&
                isScramble(s1.substring(i), s2.substring(0, m - i));
            if (ok01 || ok02) {
                memo.put(merge01, true);
                return true;
            }
        }
        memo.put(merge01, false);
        return false;
    }

}
