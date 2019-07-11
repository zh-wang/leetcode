class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] < nums[m]: # left part is sorted
                if nums[l] <= target <= nums[m]: # answer in the left
                    r = m
                else: # otherwise, search in the right
                    l = m + 1
            else: # right part is sorted
                if nums[m+1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        return l if nums[l] == target else -1

