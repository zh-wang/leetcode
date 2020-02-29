class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        n = len(citations)
        l, r = 0, n # h is in range [0, n]
        if citations[0] >= r: # N is the h-index?
            return r
        ret = l
        while l < r: # binary search in range [0, n]. Note that 0 is always a valid answer
            m = (l + r) // 2
            if citations[n - 1 - m] >= m: # m-th item's value from the end is greater than m?
                l = m + 1 # there must be m items, whose value are greater than m, so m can be h-index
                ret = m
            else:
                r = m # otherwise, m is too large
        return ret if citations[n - l] < l else l
