# STAR

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        t = [0 for _ in range(n + 1)] # binary indexed tree
        
        sums = [(nums[0], 1)] # sum to index i, i + 1
        # the index is for binary indexed tree, so it starts from 1
        for i in range(1, n):
            sums += [(sums[-1][0] + nums[i], i + 1)]
        sums.sort()
        # lower -2, upper = 2
        # (-2, 1) (2, 3) (3, 2)
        
        def update(i, value):
            index = i + 1
            while index <= n:
                t[index] += value
                index += (index & -index)
            
        def read(i):
            ret = 0
            index = i + 1
            while index > 0:
                ret += t[index]
                index -= (index & -index)
            return ret
        
        l, r = 0, 0 # sliding window
        # because sums is sorted, sliding window can only move forward
        count = 0
        for i in range(n):
            prefix = sums[i][0]
            if lower <= prefix <= upper: # range [sums[i][1], sums[i][1]] meet the condition
                count += 1
            # We want number of index k, which
            # 1. sums[k][1] < sums[i][1]
            # 2. lo <= sums[i][0] <= hi
            # A typical way is counting k by go through l to r, but it's linear time.
            # Use binary indexed tree improves that to log time
            hi, lo = prefix - lower, prefix - upper
            while r < n and sums[r][0] <= hi:
                update(sums[r][1], 1)
                r += 1
            while l < n and sums[l][0] < lo:
                update(sums[l][1], -1)
                l += 1
            count += read(sums[i][1] - 1)

        return count
