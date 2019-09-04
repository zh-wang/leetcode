// --Link--
// [LintCode](https://www.lintcode.com/problem/read-n-characters-given-read4-ii-call-multiple-times/description)
//
/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {

    private int remain = 0;
    private int buf4_s = 0;
    private char[] buf4 = new char[4];

    /**
     * @param buf destination buffer
     * @param n maximum number of characters to read
     * @return the number of characters read
     */
    public int read(char[] buf, int n) {
        // Write your code here
        int done = 0;
        if (remain > 0) {
            int cpCnt = Math.min(n, remain);
            System.arraycopy(buf4, buf4_s, buf, 0, cpCnt);
            done = cpCnt;
            remain -= cpCnt;
        }
        while (done < n) {
            int readCnt = read4(buf4);
            if (readCnt == 0) return done;
            int cpCnt = Math.min(readCnt, n - done);
            System.arraycopy(buf4, 0, buf, done, cpCnt);
            done += cpCnt;
            buf4_s = cpCnt;
            remain = readCnt - cpCnt;
        }
        return done;
    }
}
