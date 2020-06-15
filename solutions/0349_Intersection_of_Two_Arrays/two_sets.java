class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        for (int v : nums1) {
            s1.add(v);
        }
        Set<Integer> s2 = new HashSet<>();
        for (int v : nums2) {
            s2.add(v);
        }
        s1.retainAll(s2);
        // Set => List of Integer => Stream => List of int => int[]
        return (new ArrayList<>(s1)).stream().mapToInt(i->i).toArray();
    }
}
