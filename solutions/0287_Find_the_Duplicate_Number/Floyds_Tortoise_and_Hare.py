import functools

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        p1, p2 = nums[0], nums[0]
        p1 = nums[p1]
        p2 = nums[nums[p2]]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[nums[p2]]

        p1 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
