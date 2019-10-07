class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = list(sorted(nums))
        i, j = ((len(nums) + 1) // 2) - 1, len(nums) - 1
        t = 0
        # s => [x,x,x,x,x,y,y,y,y]
        #               ^       ^
        #               i       j  <= pick nums[i] and nums[j] from
        #             ^       ^
        #             i       j
        while t < len(nums) - 1:
            nums[t] = s[i]
            nums[t+1] = s[j]
            t += 2
            i, j = i-1, j-1
        if t < len(nums):
            nums[t] = s[i]
