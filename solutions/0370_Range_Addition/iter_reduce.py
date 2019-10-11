// --Link--
// https://www.lintcode.com/problem/range-addition/description

from functools import reduce

class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        vals = [0 for _ in range(length)]
        for u in updates:
            vals[u[0]] += u[2]
            if u[1] < len(vals) - 1:
                vals[u[1]+1] += -u[2]
        for i in range(1, len(vals)):
            vals[i] += vals[i-1]
        return vals
