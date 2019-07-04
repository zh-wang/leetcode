class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.exchange(nums, 1, 0)
        self.exchange(nums, 2, 0)
        self.exchange(nums, 2, 1)

    def exchange(self, nums, x, y):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] != x:
                i += 1
            while i < j and nums[j] != y:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
