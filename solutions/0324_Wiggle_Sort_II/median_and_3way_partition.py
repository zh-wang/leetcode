from typing import *
import random as rd

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get median
        m = self.kth_largest(nums, 0, len(nums)-1, len(nums)//2)
        vindex = [(1 + 2*i) % (len(nums) | 1) for i in range(len(nums))]
        # 3way partition - descending
        i, j = 0, 0
        n = len(nums) - 1
        while j <= n:
            if nums[vindex[j]] > m:
                nums[vindex[i]], nums[vindex[j]] = nums[vindex[j]], nums[vindex[i]]
                i, j = i+1, j+1
            elif nums[vindex[j]] < m:
                nums[vindex[j]], nums[vindex[n]] = nums[vindex[n]], nums[vindex[j]]
                n -= 1
            else:
                j += 1

    def kth_largest(self, nums, l, r, k):
        if l == r:
            return nums[l]
        p = rd.randrange(l, r+1) # partition between index p
        pivot = nums[p]
        nums[p], nums[r] = nums[r], nums[p] # swap pivot to right
        lowest = l
        for i in range(lowest, len(nums)):
            if nums[i] > pivot:
                nums[i], nums[lowest] = nums[lowest], nums[i]
                lowest += 1
        nums[r], nums[lowest] = nums[lowest], nums[r]

        if lowest + 1 == k:
            return nums[lowest]
        elif lowest + 1 > k:
            return self.kth_largest(nums, l, lowest-1, k)
        else:
            return self.kth_largest(nums, lowest+1, r, k)

x = [1,3,2,2,2,1,1,3,1,1,2]
Solution().wiggleSort(x)
print(x)

y = [1,5,2,5,4]
Solution().wiggleSort(y)
print(y)
