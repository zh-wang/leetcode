class Solution {
    public List<String> generateParenthesis(int n) {
        return recur("", n, 0, new ArrayList<String>());
    }

    private List<String> recur(String s, int n, int m, List<String> list) {
        if (n < 0 || m < 0) return list;
        if (n == 0 && m == 0) {
            list.add(s);
        }
        recur(s + "(", n - 1, m + 1, list);
        recur(s + ")", n, m - 1, list);
        return list;
    }
}
