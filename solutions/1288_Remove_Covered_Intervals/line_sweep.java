class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        // sort intervals by their start point in ascending order
        // if they are equal, sort by their end point in descending order
        Arrays.sort(intervals, (i1, i2) -> {
            return i1[0] == i2[0] ? i2[1] - i1[1] : i1[0] - i2[0];
        });

        int ret = 0;
        int end = intervals[0][1]; // an overall end point
        for (int i = 1; i < intervals.length; ++i) {
            // no need to check start point because they are in ascending sort
            if (intervals[i][1] <= end) { // found overlap
                ++ret;
            } else {
                end = intervals[i][1]; // update end point
            }
        }
        return intervals.length - ret;
    }
}
