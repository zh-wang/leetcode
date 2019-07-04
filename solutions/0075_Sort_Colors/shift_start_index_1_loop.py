class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s0, s1, s2 = -1, -1, -1 # start index of 0s, 1s and 2s
        # s0 only increases when 0 is found.
        # s1 increases when 0 or 1 is found.
        # s2 always increases.
        # Therefore, s0 <= s1 <= s2 always holds.(*)
        # This property guarantees that if nums[i] == 0, nums[i] will finally
        # set to 0, in the following for-if routine.
        # This also shows that s0 will finally be the number of 0 in nums,
        # and also works for s1, s2.
        for i in range(len(nums)):
            if nums[i] == 0:
                s2 += 1; nums[s2] = 2
                s1 += 1; nums[s1] = 1
                s0 += 1; nums[s0] = 0
            elif nums[i] == 1:
                s2 += 1; nums[s2] = 2
                s1 += 1; nums[s1] = 1
            else:
                s2 += 1; nums[s2] = 2
