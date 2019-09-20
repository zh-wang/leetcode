// --Link--
// https://www.lintcode.com/problem/reverse-words-in-a-string-ii/description

class Solution {
public:
    /**
     * @param str: a string
     * @return: return a string
     */
    string reverseWords(string &str) {
        // write your code here
        reverse(str, 0, str.length() - 1);
        int i = 0, j = 0;
        int n = str.length();
        while (i < n) {
            while (i < n && str[i] == ' ') ++i;
            j = i;
            while (j < n && str[j] != ' ') ++j;
            reverse(str, i, j - 1);
            i = j;
        }
        return str;
    }

    void reverse(string &s, int i, int j) {
        while (i < j) {
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
            ++i, --j;
        }
    }
};
