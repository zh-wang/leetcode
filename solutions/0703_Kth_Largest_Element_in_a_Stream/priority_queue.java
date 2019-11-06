class KthLargest {

    private PriorityQueue<Integer> q;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        q = new PriorityQueue<>();
        for (int i = 0; i < nums.length; ++i) {
            q.add(nums[i]);
        }
    }

    public int add(int val) {
        if (q.size() >= k && q.peek() > val) {
            return q.peek();
        }
        q.add(val);
        while (this.k < q.size()) {
            q.poll();
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
