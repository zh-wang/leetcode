class Solution {
    public int myAtoi(String str) {
        if (str.length() == 0) return 0;
        int ret = 0;
        int from = 0;
        while (from < str.length() && str.charAt(from) == ' ') from += 1;
        if (from >= str.length()) return 0;
        int to = str.indexOf(' ', from);
        String pat = to == -1 ? str.substring(from) : str.substring(from, to);
        boolean isMinus = false;
        from = 0;
        if (pat.charAt(0) == '-') {
            isMinus = true;
            from += 1;
        }
        if (pat.charAt(0) == '+') {
            from += 1;
        }
        int posLimit = Integer.MAX_VALUE / 10;
        int negLimit = Integer.MIN_VALUE / 10;
        while (from < pat.length() && pat.charAt(from) >= '0' && pat.charAt(from) <= '9') {
            int digit = pat.charAt(from) - '0';
            if (isMinus) digit = -digit;
            if (ret > posLimit || (ret == posLimit && digit > 7)) return Integer.MAX_VALUE;
            if (ret < negLimit || (ret == negLimit && digit < -8)) return Integer.MIN_VALUE;
            ret = ret * 10 + digit;
            from += 1;
        }
        return ret;
    }
}
