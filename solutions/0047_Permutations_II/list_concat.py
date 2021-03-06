class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for v in nums:
            new_perms = []
            for p in perms:
                for i in range(0, len(p) + 1): # insert v in position 0, 1, 2, ...
                    new_perms.append(p[:i] + [v] + p[i:])
                    if i < len(p) and v == p[i]:
                        break # only allow v to be inserted before its duplicates
            perms = new_perms
        return perms
