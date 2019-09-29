class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse_in_space(nums, 0, len(nums)-1)
        self.reverse_in_space(nums, 0, k-1)
        self.reverse_in_space(nums, k, len(nums)-1)

    def reverse_in_space(self, nums, l, r):
        for i in range((r-l+1)//2):
            nums[l+i], nums[r-i] = nums[r-i], nums[l+i]
