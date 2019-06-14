class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        # inc list by 1, or we need to move v to (v-1)th slot
        # which is not so clear in implementation
        nums.append(0)
        for i in range(len(nums)): # move v to v-th slot
            v = nums[i]
            if v > 0:
                while i != v and v > 0 and v < len(nums):
                    temp = nums[v] # save target slot's value in temp
                    nums[v] = v # write target slot
                    i = v # next i will be v
                    v = temp # next v will be the value saved above
        # nums become [@, 1, 2, 3, ...] or [@, x, x, 4, ...]
        # @ can be any value, which do not affect the answer
        for i in range(1, len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
