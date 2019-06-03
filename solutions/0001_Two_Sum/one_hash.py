class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checker = {}
        for i, num in enumerate(nums):
            if (target - num) in checker.keys():
                j = checker[target - num]
                return [j, i]
            else:
                checker[num] = i
        return [-1, -1]
