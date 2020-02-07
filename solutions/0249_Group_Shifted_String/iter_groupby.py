# --Link--
# https://www.geeksforgeeks.org/group-shifted-string/

import itertools
from collections import defaultdict

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def groupShiftString(self, strs):
        # write your code here
        groupByHash = defaultdict(lambda: [])
        for str in strs:
            groupByHash[self.cal(str)] += [str]
        return [ myList for myList in groupByHash.values() ]

    def cal(self, str):
        if not str:
            return -1
        shift = -1
        ret = 0
        for c in str:
            if shift == -1:
                shift = ord(c) - ord('a')
            ret += ret * 31 + (ord(c) - shift)
        return ret

x = Solution().groupShiftString(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"])
print(x)
