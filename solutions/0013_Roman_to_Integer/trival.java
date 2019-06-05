class Solution {
    public int romanToInt(String s) {
        String[] kws = {"M", "CM", "D","CD",
                        "C", "XC", "L", "XL",
                        "X", "IX", "V", "IV", "I"};
        int[] vs = {1000, 900, 500, 400,
                    100, 90, 50, 40,
                    10, 9, 5, 4, 1};
        int ret = 0;
        int from = 0;
        while (from < s.length()) {
            int i = 0;
            int newFrom = 0;
            while (i < kws.length && (newFrom = s.indexOf(kws[i], from)) != from) ++i;
            ret += vs[i];
            from += kws[i].length();
        }
        return ret;
    }
}
