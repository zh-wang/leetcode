class KthLargest {

    private PriorityQueue<Integer> q;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        q = new PriorityQueue<>();
        for (int i = 0; i < k && i < nums.length; ++i) {
            q.add(nums[i]);
        }
        for (int i = k; i < nums.length; ++i) {
            this.add(nums[i]);
        }
    }

    public int add(int val) {
        if (q.size() < this.k) {
            q.add(val);
            return q.peek();
        }
        if (val > q.peek()) {
            q.poll();
            q.add(val);
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
