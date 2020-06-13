class Solution {
    public String reverseVowels(String s) {
        char[] c = new char[s.length()];
        for (int i = 0; i < s.length(); ++i) {
            c[i] = s.charAt(i);
        }
        int i = 0;
        int j = c.length - 1;
        while (i < j) {
            while (i < j && !isVowel(c[i])) ++i;
            while (i < j && !isVowel(c[j])) --j;
            if (i < j) {
                char t = c[i];
                c[i] = c[j];
                c[j] = t;
                ++i;
                --j;
            }
        }
        return new String(c);
    }

    private boolean isVowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            return true;
        }
        return false;
    }
}
