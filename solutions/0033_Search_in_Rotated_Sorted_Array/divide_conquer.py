class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        ret = self.trickBFS(nums, target, 0, len(nums) - 1)
        return ret

    def trickBFS(self, nums, target, l, r):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return - 1
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] < nums[m]: # left part is sorted
            if nums[l] <= target <= nums[m]: # answer in the left
                return self.trickBFS(nums, target, l, m)
            else: # otherwise, search in the right
                return self.trickBFS(nums, target, m+1, r)
        else: # right part is sorted
            if nums[m+1] <= target <= nums[r]:
                return self.trickBFS(nums, target, m+1, r)
            else:
                return self.trickBFS(nums, target, l, m)
