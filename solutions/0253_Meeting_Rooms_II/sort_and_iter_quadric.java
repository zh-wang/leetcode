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

        List<Interval> rooms = new ArrayList<>();
        rooms.add(intervals.get(0));

        // for each interval, we want find a room to fit
        for (int i = 1; i < intervals.size(); ++i) {
            boolean foundRoom = false;
            // for each room we prepared
            for (int j = 0; j < rooms.size(); ++j) {
                // if we can find a room which is NOT overlapped with an interval
                // we can extend the room's ocupied time to the end of that interval
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
