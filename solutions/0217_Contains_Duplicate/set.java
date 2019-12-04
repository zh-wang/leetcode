class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (Integer v : nums) {
            if (set.contains(v)) return true;
            else set.add(v);
        }
        return false;
    }
}
