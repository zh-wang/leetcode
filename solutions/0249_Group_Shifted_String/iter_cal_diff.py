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
        if len(str) == 1:
            return ''
        ret = ''
        for i in range(1, len(str)):
            ret += chr( (ord(str[i]) - ord(str[i-1])) % 26 )
        return ret

x = Solution().groupShiftString(["acd", "dfg", "wyz", "yab", "mop", "ife",  "bdfh", "a", "x", "moqs"])
print(x)
