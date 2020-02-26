class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, v in enumerate(nums):
            missing ^= i ^ nums[i]
        return missing
