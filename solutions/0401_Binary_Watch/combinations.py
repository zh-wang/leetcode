from typing import *

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        l = [i for i in range(10)]
        ret = [[]]
        for _ in range(num):
            new_ret = []
            for x in ret:
                for y in range(x[-1] + 1 if x else 0, len(l)):
                    new_ret += [x + [y]]
            ret = new_ret

        ret2 = []
        mapper = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        for l in ret:
            hour, minute = 0, 0
            for mi in l:
                if mi < 4:
                    hour += mapper[mi]
                else:
                    minute += mapper[mi]
            if hour < 12 and minute < 60:
                ret2 += ["%d:%02d" % (hour, minute)]
        return ret2
