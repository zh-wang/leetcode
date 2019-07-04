class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s0, s2 = 0, len(nums) - 1 # index of next 0 or 2
        i = 0
        while i < len(nums):
            if nums[i] == 0: # exchange 0 to head
                nums[i], nums[s0] = nums[s0], nums[i]
                s0 += 1
            elif nums[i] == 2 and i < s2: # exchange 2 to tail
                nums[i], nums[s2] = nums[s2], nums[i]
                s2 -= 1
                # This is a forward exchange, so we
                # need to check the exchanged value.
                # So dec index by 1.
                # Note that this may occur several time on same index i
                i -= 1
            i += 1
