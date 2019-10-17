# ⭐️ --Link--
# https://www.lintcode.com/problem/missing-ranges/description

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        if lower > upper:
            return []
        ret = []
        pre = lower - 1
        for i in range(len(nums) + 1): # this even handles nums=[]
            after = nums[i] if i < len(nums) else upper + 1
            if pre + 2 == after:
                ret += ['%d' % (pre + 1)]
            elif pre + 2 < after:
                ret += ['%d->%d' % (pre + 1, after - 1)]
            pre = after
        return ret

