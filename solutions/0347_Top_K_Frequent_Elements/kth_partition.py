from collections import defaultdict
import random as rd

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(int)
        for v in nums:
            counters[v] += 1
        arr = [ (v, k) for k, v in counters.items() ] # dict of cnt => num
        if len(arr) == k: # k is large enough to take all nums
            return list(counters.keys())
        p = self.kthPartition(arr, 0, len(arr) - 1, len(arr) - k)
        return [ tup[1] for tup in arr[p + 1:] ]

    def kthPartition(self, arr, l, r, k):
        p = rd.randrange(l, r + 1)
        pivot = arr[p][0]
        arr[p], arr[r] = arr[r], arr[p]
        lowest = l
        for i in range(lowest, r + 1):
            if arr[i][0] < pivot:
                arr[i], arr[lowest] = arr[lowest], arr[i]
                lowest += 1
        arr[lowest], arr[r] = arr[r], arr[lowest]

        if lowest + 1 == k:
            return lowest
        elif lowest + 1 > k:
            return self.kthPartition(arr, l, lowest - 1, k)
        else:
            return self.kthPartition(arr, lowest + 1, r, k)
