class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.l = []
        self.recur(nums, 0)
        return self.ret

    def recur(self, nums, start_index):
        if start_index >= len(nums):
            self.ret.append(self.l[:])
            return
        for i in range(start_index, len(nums)):
            self.l.append(nums[i])
            nums[start_index], nums[i] = nums[i], nums[start_index]
            self.recur(nums, start_index + 1)
            nums[start_index], nums[i] = nums[i], nums[start_index]
            self.l.pop()
