class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        l, r = 0, len(nums) - 1
        while l < r:
            # Make nums[l] not equals to nums[r].
            while l < r and nums[l] == nums[r]:
                l += 1
            # If all of the elements are the same
            if l == r:
                break
            m = (l + r) // 2
            if nums[m] == target:
                return True
            # Note that in 0033, we only need `<`, not `<=`
            if nums[l] <= nums[m]: # left part is sorted
                if nums[l] <= target <= nums[m]: # answer in the left
                    r = m
                else: # otherwise, search in the right
                    l = m + 1
            else: # right part is sorted
                if nums[m+1] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        return nums[l] == target
