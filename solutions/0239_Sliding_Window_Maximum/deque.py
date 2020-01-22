# STAR

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # an index queue. The value of them are in decreasing order.
        ret = []
        for i, v in enumerate(nums):
            # pop from end, until some value is larger than current value(v)
            # This keep q in decreasing order
            while q and nums[q[-1]] < v:
                q.pop()
            q += [i]
            if q[0] == i - k: # if the leftmost one is out of window, remove it
                q.popleft()
            if i >= k - 1: # the leftmost one is always largest. Add it to answer
                ret += [ nums[q[0]] ]
        return ret
