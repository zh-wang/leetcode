class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        ret = [pre + ([nums[-1]] if choose else []) for pre in self.subsets(nums[:-1]) for choose in [True, False]]
        return ret
