class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int v : nums1) {
            counter.put(v, counter.getOrDefault(v, 0) + 1);
        }
        List<Integer> ret = new ArrayList<>();
        for (int v : nums2) {
            if (counter.containsKey(v) && counter.get(v) > 0) {
                ret.add(v);
                counter.put(v, counter.get(v) - 1);
            }
        }
        return ret.stream().mapToInt(i->i).toArray();
    }
}
