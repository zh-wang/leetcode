class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (i1, i2) -> {
            return i1[0] == i2[0] ? i2[1] - i1[1] : i1[0] - i2[0];
        });

        int ret = 0;
        int end = intervals[0][1];
        for (int i = 1; i < intervals.length; ++i) {
            if (intervals[i][1] <= end) {
                ++ret;
            } else {
                end = intervals[i][1];
            }
        }
        return intervals.length - ret;
    }
}
