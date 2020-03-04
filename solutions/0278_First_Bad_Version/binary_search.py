# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        v = l
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                v = m
                r = m
            else:
                l = m + 1
        return l if isBadVersion(l) else v
