class Solution {
    public String countAndSay(int n) {
        String s = "1";
        for (int i = 1; i < n; ++i) {
            StringBuilder sb = new StringBuilder();
            int cnt = 1;
            char c = s.charAt(0);
            for (int j = 1; j < s.length(); ++j) {
                if (s.charAt(j) == c) {
                    cnt += 1;
                } else {
                    sb.append(cnt);
                    sb.append(c);
                    c = s.charAt(j);
                    cnt = 1;
                }
            }
            if (cnt > 0) {
                sb.append(cnt);
                sb.append(c);
            }
            s = sb.toString();
        }
        return s;
    }
}
