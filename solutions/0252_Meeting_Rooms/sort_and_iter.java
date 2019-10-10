// --Link--
// https://www.lintcode.com/problem/meeting-rooms/description

/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    public boolean canAttendMeetings(List<Interval> intervals) {
        // Write your code here
        Collections.sort(intervals, (v1, v2) -> {
            if (v1.start < v2.start) return -1;
            else if (v1.start > v2.start) return 1;
            else return 0;
        });
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals.get(i).start < intervals.get(i-1).end) {
                return false;
            }
        }
        return true;
    }
}
