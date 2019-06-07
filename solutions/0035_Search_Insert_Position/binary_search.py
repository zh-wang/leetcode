class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0
        if target > nums[-1]: return len(nums)
        return self.bi_search(nums, target, 0, len(nums) - 1)

    def bi_search(self, nums, target, l, r):
        if l == r:
            return l
        m = (l + r) // 2
        if target <= nums[m]:
            return self.bi_search(nums, target, l, m)
        else:
            return self.bi_search(nums, target, m+1, r)
