class Solution {
public:
    string reverseWords(string s) {
        reverse(s, 0, s.length() - 1);

        int i = 0, j = 0; // start & end for each word
        int p = 0; // start position for lShift
        while (i < s.length()) {
            while (i < s.length() && s[i] == ' ') ++i;
            if (s[i] == '\0') break;
            j = i;
            while (j < s.length() && s[j] != ' ') ++j;
            // printf("%d, %d\n", i, j);
            reverse(s, i, j - 1);
            if (p > 0) { // the first word do not need a space
                s[p] = ' ';
                ++p;
            }
            p += lShift(s, p, i, j - 1); // go to next p
            i = j + 1;
        }
        s.resize(p);
        return s;
    }

    void reverse(string &s, int i, int j) {
        while (i < j) {
            char c = s[i];
            s[i] = s[j];
            s[j] = c;
            ++i, --j;
        }
    }

    // move s[i:j] to index [p:p+j-i]
    // return size of s[i:j]
    int lShift(string &s, int p, int i, int j) {
        if (p == i) return j - i + 1;
        int k = i;
        while (k <= j) {
            s[p] = s[k];
            ++p, ++k;
        }
        return j - i + 1;
    }
};
