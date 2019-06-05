class Solution {
    public String intToRoman(int num) {
        int a = num % 10;
        int b = (num / 10) % 10;
        int c = (num / 100) % 10;
        int d = (num / 1000) % 10;
        StringBuilder sb = new StringBuilder();
        // 4th digit
        for (int i = 0; i < d; ++i) sb.append('M');
        // 3rd dight
        sb.append(makeStr(c, 'C', 'D', 'M'));
        // 2nd digit
        sb.append(makeStr(b, 'X', 'L', 'C'));
        // 1st
        sb.append(makeStr(a, 'I', 'V', 'X'));
        return sb.toString();
    }

    // I, II, III, VI, V, VI, VII, VIII, IX, X
    private String makeStr(int n, char x, char y, char z) {
        StringBuilder sb = new StringBuilder();
        if (n == 9) {
            sb.append(x);
            sb.append(z);
        } else if (n >= 5) {
            sb.append(y);
            for (int i = 6; i <= n; ++i) sb.append(x);
        } else if (n == 4) {
            sb.append(x);
            sb.append(y);
        } else {
            for (int i = 1; i <= n; ++i) sb.append(x);
        }
        return sb.toString();
    }
}
