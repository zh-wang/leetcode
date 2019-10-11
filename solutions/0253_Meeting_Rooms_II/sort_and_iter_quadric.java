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

        // PriorityQueue<Integer> minq = new PriorityQueue<>();
        // minq.push(intervals.get(0));
        // for (int i = 1; i < intervals.size(); ++i) {

        // }
        List<Interval> rooms = new ArrayList<>();
        rooms.add(intervals.get(0));

        for (int i = 1; i < intervals.size(); ++i) {
            boolean foundRoom = false;
            for (int j = 0; j < rooms.size(); ++j) {
                if (rooms.get(j).end <= intervals.get(i).start) {
                    rooms.get(j).end = intervals.get(i).end;
                    foundRoom = true;
                    break;
                }
            }
            if (!foundRoom) {
                rooms.add(intervals.get(i));
            }
        }
        return rooms.size();
    }
}
