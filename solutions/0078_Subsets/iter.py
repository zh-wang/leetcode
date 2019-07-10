class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        tf = [True, False]
        for v in nums:
            ret = [pre + ([v] if choose else []) for pre in ret for choose in tf]
        return ret
