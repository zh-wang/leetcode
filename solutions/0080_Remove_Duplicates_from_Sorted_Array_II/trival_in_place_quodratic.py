class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 0
        for i in range(len(nums)):
            dup = False
            for j in range(end):
                if nums[i] == nums[j]:
                    dup = True
                    break
            if not dup:
                nums[end] = nums[i]
                end += 1
        return end
