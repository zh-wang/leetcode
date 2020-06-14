class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Integer> counters = new HashMap<>();
        for (int v : nums1) {
            counters.put(v, counters.getOrDefault(v, 0) + 1);
        }
        Set<Integer> ret = new HashSet<>();
        for (int v : nums2) {
            if (counters.containsKey(v) && counters.get(v) > 0) {
                ret.add(v);
                counters.put(v, counters.get(v) - 1);
            }
        }
        // Set => List of Integer => Stream => List of int => int[]
        return (new ArrayList<Integer>(ret)).stream().mapToInt(i->i).toArray();
    }
}
