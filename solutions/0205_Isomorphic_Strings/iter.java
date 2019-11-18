class Solution {
    public boolean isIsomorphic(String s, String t) {
        return checkIsomorphic(s, t) && checkIsomorphic(t, s);
    }

    private boolean checkIsomorphic(String s, String t) {
        Map<Character, Character> checker = new HashMap<>();
        int m = s.length();
        for (int i = 0; i < m; ++i) {
            if (checker.containsKey(s.charAt(i))) {
                if (checker.get(s.charAt(i)) != t.charAt(i)) {
                    return false;
                }
            } else {
                checker.put(s.charAt(i), t.charAt(i));
            }
        }
        return true;
    }
}
