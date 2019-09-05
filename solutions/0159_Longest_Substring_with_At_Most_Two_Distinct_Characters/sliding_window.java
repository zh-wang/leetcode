public class Solution {
    /**
     * @param s: A string
     * @param k: An integer
     * @return: An integer
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        // write your code here
        if (k == 0) return 0;
        int j = 0;
        int best = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); ++i) {
            char ci = s.charAt(i);
            if (map.size() < k) {
                int count = map.getOrDefault(ci, 0);
                map.put(ci, count + 1);
            } else {
                if (map.containsKey(ci)) {
                    map.put(ci, map.get(ci) + 1);
                } else {
                    while (map.size() >= k && j < i) {
                        char cj = s.charAt(j);
                        if (map.get(cj) > 1) {
                            map.put(cj, map.get(cj) - 1);
                        } else {
                            map.remove(cj);
                        }
                        j += 1;
                    }
                    map.put(ci, 1);
                }
            }
            best = Math.max(best, i - j + 1);
        }
        return best;
    }
}
