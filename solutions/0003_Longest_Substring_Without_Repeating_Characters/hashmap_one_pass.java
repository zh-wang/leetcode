// STAR

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int best = 0;
        int start = -1;
        for (int i = 0; i < s.length(); i++) { // each char l to r
            Character c = s.charAt(i);
            // If current char has been found before i
            // we have to move start point to i
            if (map.containsKey(c) && map.get(c) > start) {
                start = map.get(c);
            }
            map.put(c, i);
            best = Math.max(best, i - start);
        }
        return best;
    }
}
