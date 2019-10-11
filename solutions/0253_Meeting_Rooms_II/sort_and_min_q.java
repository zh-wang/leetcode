// --Link--
// https://www.lintcode.com/problem/meeting-rooms-ii/description

/**
 * Definition of Interval:
 * public classs Interval {
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
     * @return: the minimum number of conference rooms required
     */
    public int minMeetingRooms(List<Interval> intervals) {
        // Write your code here
        if (intervals.size() == 0) return 0;

        Collections.sort(intervals, (v1, v2) -> {
            if (v1.start < v2.start) return -1;
            else if (v1.start > v2.start) return 1;
            else return 0;
        });

        PriorityQueue<Interval> minq = new PriorityQueue<>((v1, v2) -> {
            if (v1.end < v2.end) return -1;
            else if (v1.end > v2.end) return 1;
            else return 0;
        });
        minq.add(intervals.get(0));

        for (int i = 1; i < intervals.size(); ++i) {
            if (minq.peek().end <= intervals.get(i).start) {
                Interval ivt = minq.poll();
                ivt.end = intervals.get(i).end;
                minq.add(ivt);
            } else {
                minq.add(intervals.get(i));
            }
        }
        return minq.size();
    }
}
