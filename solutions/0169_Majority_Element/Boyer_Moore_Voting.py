class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = 0
        for v in nums:
            if r == 0 or nums[r-1] == v:
                nums[r] = v
                r += 1
            elif nums[r-1] != v:
                r -= 1
            return nums[0]
