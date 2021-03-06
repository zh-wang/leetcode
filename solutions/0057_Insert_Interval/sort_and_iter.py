class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find the insertion position
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        # insert the new interval
        intervals.insert(i, newInterval)

        # do the same as 0056
        ret = []
        last = intervals[0]
        for i in range(len(intervals)):
            if last[0] <= intervals[i][0] <= last[1]:
                last = (last[0], max(intervals[i][1], last[1]))
            else:
                ret.append(last[:])
                last = intervals[i]
        ret.append(last[:])
        return ret

