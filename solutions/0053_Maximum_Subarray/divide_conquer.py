# Note that this will cause [Time Limit Exceeded] on OJ
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, s, t):
        if s == t:
            return nums[s]
        m = (s + t) // 2
        l_best, l, l_temp = -1<<32, m, 0
        while l >= 0:
            l_temp += nums[l]
            l_best = max(l_best, l_temp)
            l -= 1
        r_best, r, r_temp = -1<<32, m + 1, 0
        while r <= t:
            r_temp += nums[r]
            r_best = max(r_best, r_temp)
            r += 1
        return max(l_best + r_best, \
                  self.binarySearch(nums, s, m), \
                  self.binarySearch(nums, m + 1, t))
