import random as rd

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.find(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def find(self, nums, l, r, k):
        p = rd.randrange(l, r + 1)
        pivot = nums[p]
        nums[p], nums[r] = nums[r], nums[p]
        lowest = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[lowest] = nums[lowest], nums[i]
                lowest += 1
        nums[r], nums[lowest] = nums[lowest], nums[r]

        if lowest + 1 == k:
            return nums[lowest]
        elif lowest + 1 > k:
            return self.find(nums, l, lowest-1, k)
        else:
            return self.find(nums, lowest+1, r, k)
