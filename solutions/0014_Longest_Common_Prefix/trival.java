class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        int si = 0;
        int sl = strs[0].length();
        // find the shortest str
        for (int i = 0; i < strs.length; ++i) {
            if (strs[i].length() < sl) {
                sl = strs[i].length();
                si = i;
            }
        }
        // compare the shortest to others
        for (int i = 0; i < sl; ++i) {
            char c = strs[si].charAt(i);
            for (String s : strs) {
                if (s.charAt(i) != c) {
                    return s.substring(0, i);
                }
            }
        }
        return strs[si];
    }
}
