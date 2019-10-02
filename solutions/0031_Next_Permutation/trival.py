class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ===================
        # 1, 2, 4, 3
        #    ^
        # 1, 3, 2, 4
        # ===================
        # 1, 4, 2, 3
        #       ^
        # 1, 4, 3, 2
        # ===================

        if len(nums) == 1: return
        # find a decreasing pair, from right to left.
        # (This will find 2 in both examples)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # if we cannot find such i, then the nums is the largest one in all permutation
        if i < 0:
            nums[:] = sorted(nums) # sort to get the smallest
            return
        # if we can find i, then we want the mininum index j, nums[j] > nums[i]
        # we search j from right to left
        # *** such j always exists because a decreasing pair is found by the first step ***
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = sorted(nums[i + 1 :])
