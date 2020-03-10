class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k += 1
            elif k > 0:
                nums[i - k] = nums[i]
        for i in range(len(nums)-1, len(nums)-k-1, -1):
            nums[i] = 0
