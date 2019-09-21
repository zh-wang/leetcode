class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> set = new HashSet<>();
        Set<String> ret = new HashSet<>();
        for (int i = 0; i < s.length() - 9; ++i) {
            String sub = s.substring(i, i + 10);
            System.out.println(sub);
            if (!set.add(sub)) {
                ret.add(sub);
            }
        }
        return new ArrayList(ret);
    }
}
