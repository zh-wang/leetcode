class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        # sort with intervals' start point
        intervals = sorted(intervals)
        ret = []
        # <------>
        #     <------->
        #            <----->
        # ^-last-^
        last = intervals[0] # next MERGED interval which will be added into ret
        for i in range(len(intervals)):
            # update last if we found an interval which can be merged into it
            if last[0] <= intervals[i][0] <= last[1]:
                last = (last[0], max(intervals[i][1], last[1]))
            else: # otherwise, insert last then allocate a new last
                ret.append(last[:])
                last = intervals[i]
        ret.append(last[:])
        return ret
