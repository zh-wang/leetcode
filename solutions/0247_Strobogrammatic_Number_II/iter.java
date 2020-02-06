public class Solution {

    String[] nums = {"0", "1", "6", "8", "9"};
    String[] numsNonFirst = {"1", "6", "8", "9"};
    String[] mids = {"0", "1", "8"};

    Map<Character, String> rev = new HashMap<Character, String>() {{
        put('0', "0");
        put('1', "1");
        put('6', "9");
        put('8', "8");
        put('9', "6");
    }};

    /**
     * @param n: the length of strobogrammatic number
     * @return: All strobogrammatic numbers
     */
    public List<String> findStrobogrammatic(int n) {
        // write your code here
        List<String> ret = new ArrayList<>();
        List<String> emptyList = new ArrayList<>();
        emptyList.add("");
        List<String> firstHalf = generate(0, n / 2, emptyList);
        for (String s : firstHalf) {
            String t = "";
            for (char c : s.toCharArray()) {
                t = rev.get(c) + t;
            }
            if ((n & 1) == 1) {
                for (String mid : mids) {
                    ret.add(s + mid + t);
                }
            } else {
                ret.add(s + t);
            }
        }
        return ret;
    }

    private List<String> generate(int step, int k, List<String> list) {
        if (step == k) {
            return list;
        }
        List<String> nextList = new ArrayList<>();
        for (String num : (step == 0 ? numsNonFirst : nums)) {
            for (String s : list) {
                nextList.add(s + num);
            }
        }
        return generate(step + 1, k, nextList);
    }
}
