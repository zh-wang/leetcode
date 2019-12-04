class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> a - b);
        for (Integer v : nums) {
            q.add(v);
            if (q.size() > k) {
                q.poll();
            }
        }
        return q.poll();
    }
}
