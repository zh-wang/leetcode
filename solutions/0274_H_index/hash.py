import collections

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        count = collections.defaultdict(int)
        for c in citations:
            count[c] += 1
        # s_count is a dict of (#paper's citation, #paper)
        s_count = [(k, count[k]) for k in sorted(count.keys(), reverse=True)]
        n = len(citations) # total #paper
        k = 0 # #paper whose citations >= h
        for i in range(len(s_count)):
            h, ct = s_count[i]
            k += ct
            if k >= h: # #papar is more than #citations
                return h # we know that remaining papers will have no more than h citations
            # otherwise, we should return k only if k >= next smaller citation, or no next exists
            elif i == len(s_count) - 1 or k >= s_count[i+1][0]:
                return k
        return n
