class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for v in nums:
            perms = [p[:i] + [v] + p[i:] \
                        for p in perms \
                        for i in range( (p + [v]).index(v) + 1 )]
        return perms
