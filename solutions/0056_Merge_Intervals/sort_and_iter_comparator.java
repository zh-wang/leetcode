class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> ret = new ArrayList<>();
        if (intervals == null || intervals.length == 0) {
            return ret.toArray(new int[0][]);
        }
        Arrays.sort(intervals, Comparator.comparingInt((int[] itv) -> itv[0]));
        int[] last = intervals[0];
        for (var itv : intervals) {
            if (last[0] <= itv[0] && itv[0] <= last[1]) {
                last[1] = Math.max(last[1], itv[1]);
            } else {
                ret.add(last);
                last = itv;
            }
        }
        ret.add(last);
        return ret.toArray(new int[0][]);
    }
}
