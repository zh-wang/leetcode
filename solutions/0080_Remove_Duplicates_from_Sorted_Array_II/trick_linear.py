class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 0
        for v in nums:
            if end < 2 or v > nums[end - 2]:
                nums[end] = v
                end += 1
        return end
