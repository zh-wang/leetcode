class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if target < nums[0] * 3: # target is too small
            return nums[0] + nums[1] + nums[2]
        if target > nums[-1] * 3: # target is too large
            return nums[-1] + nums[-2] + nums[-3]
        n = len(nums)
        i = 0
        best = 1 << 30
        ret = 0
        while i < n - 2:
            l = i + 1
            r = n - 1
            # The following part can be added to reduce comparison,
            # but it does not affect running time a lot
            #
            # if target < nums[i] * 3 and best == (1 << 30):
            #     return nums[i] + nums[i + 1] + nums[i + 2]
            # if target > nums[r] * 3 and best == (1 << 30):
            #     return nums[r] + nums[r - 1] + nums[r - 2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return target
                diff = abs(total - target)
                if diff < best:
                    best = diff
                    ret = total
                if total > target:
                    r -= 1
                else:
                    l += 1
            while i < n - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ret
