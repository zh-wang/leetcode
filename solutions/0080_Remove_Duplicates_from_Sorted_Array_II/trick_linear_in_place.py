# STAR

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 0 # current end index
        for v in nums:
            # if end index < 2, appearently no duplicates
            # if current number > nums[end - 2], e.g. ...2,2,3
            #                                                ^end index
            # therefore, there is no duplicates in this case
            if end < 2 or v > nums[end - 2]:
                nums[end] = v # move current number to end index
                end += 1 # inc end index
        return end
