from collections import defaultdict
from itertools import permutations

class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        # write your code here
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        check = [k for k in counts.keys() if counts[k] % 2 == 1]
        if len(check) > 1:
            return []
        center = '' if len(check) == 0 else check[0]
        nums = ''
        for k in counts.keys():
            nums += (k * (counts[k] // 2))
        return [''.join(s + [center] + list(reversed(s))) for s in self.permuteUnique(nums)]

    # return List[List['']]
    def permuteUnique(self, nums):
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
