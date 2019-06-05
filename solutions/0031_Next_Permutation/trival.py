class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        # find the start index to do permutation
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # the nums is the largest one in all permutation
        if i < 0:
            nums[:] = sorted(nums) # sort to get the smallest
            return
        j = len(nums) - 1 # find the mininum number from i, which is larger than nums[i]
        while j > 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = sorted(nums[i + 1 :])
