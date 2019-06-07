class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        lowest = self.bi_search_lowest(nums, target, 0, len(nums) - 1)
        if lowest == -1: return [-1, -1]
        highest = self.bi_search_highest(nums, target, 0, len(nums) - 1)
        ret = [lowest, highest]
        return ret

    def bi_search_lowest(self, nums, target, l, r):
        if l == r:
            return l if nums[l] == target else -1
        m = (l + r) // 2
        if target <= nums[m]:
            return self.bi_search_lowest(nums, target, l, m)
        else:
            return self.bi_search_lowest(nums, target, m+1, r)

    def bi_search_highest(self, nums, target, l, r):
        if l == r:
            return l if nums[l] == target else -1
        m = (l + r) // 2
        if target > nums[m]:
            return self.bi_search_highest(nums, target, m+1, r)
        elif target == nums[m]:
            if nums[m+1] > target: return m
            else: return self.bi_search_highest(nums, target, m+1, r)
        else:
            return self.bi_search_highest(nums, target, l, m)
