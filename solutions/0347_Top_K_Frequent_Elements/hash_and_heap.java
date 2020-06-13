class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int v : nums) {
            int c = counter.getOrDefault(v, 0) + 1;
            counter.put(v, c);
        }

        PriorityQueue<Box> q = new PriorityQueue<>((a, b) -> (a.c - b.c));
        for (Integer i : counter.keySet()) {
            q.add(new Box(i, counter.get(i)));
            if (q.size() > k) {
                q.poll();
            }
        }

        int[] ret = new int[k];
        int i = 0;
        while (q.size() > 0) {
            Box box = q.poll();
            ret[++i] = box.v;
        }

        return ret;
    }

    private static class Box {
        int v;
        int c;

        public Box(int v, int c) {
            this.v = v;
            this.c = c;
        }
    }
}
