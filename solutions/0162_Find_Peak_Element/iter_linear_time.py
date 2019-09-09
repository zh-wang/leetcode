class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        hasInc = False # has an increasing pair is found?
        for i in range(1, len(nums)):
            if hasInc and nums[i] < nums[i-1]:
                return i-1
            if nums[i] > nums[i-1]:
                hasInc = True
        # if an increasing pair if found but program does not return in for loop,
        # means that nums is a sorted inc array, return the last index
        # Otherwise, nums is a sorted dec array, return the first index
        return len(nums)-1 if hasInc else 0
