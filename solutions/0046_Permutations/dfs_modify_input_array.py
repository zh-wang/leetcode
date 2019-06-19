class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        # no need an additional list to store temp answer
        # temp anwser will be filled in nums
        self.recur(nums, 0)
        return self.ret

    def recur(self, nums, start_index):
        # the left of nums before start_index will always be a composed perm
        # the right will always be a working list
        if start_index >= len(nums):
            self.ret.append(nums[:])
            return
        for i in range(start_index, len(nums)):
            nums[start_index], nums[i] = nums[i], nums[start_index]
            self.recur(nums, start_index + 1)
            nums[start_index], nums[i] = nums[i], nums[start_index]
