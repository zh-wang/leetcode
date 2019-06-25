class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals)
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
