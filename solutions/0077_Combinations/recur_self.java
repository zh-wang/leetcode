class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ret = new ArrayList<>();
        if (k == 0) {
            ret.add(new ArrayList<>());
            return ret;
        }
        for (int i = k; i <= n; ++i) {
            for (var li : combine(i - 1, k - 1)) {
                li.add(i);
                ret.add(new ArrayList<>(li));
            }
        }
        return ret;
    }
}
