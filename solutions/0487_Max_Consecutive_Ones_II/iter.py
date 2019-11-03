class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here

        # build an array of 1's count
        # [1, 0, 1, 1, 0] => [1, 2]
        counts, cur = [], 0
        for v in nums:
            if v == 0:
                counts += [cur]
                cur = 0
            else:
                cur += 1
        if cur > 0:
            counts += [cur]

        # find answer with count array
        best = 0
        for i in range(len(counts)-1):
            best = max(best, counts[i] + counts[i+1] + 1)
        return best
