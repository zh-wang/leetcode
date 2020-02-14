from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        if min_num < 0:
            nums = [v - min_num for v in nums]
        xor_ret = reduce(lambda x, y: x ^ y, nums, 0)
        # find a bit which is different in those two numbers
        k = 1
        while k < xor_ret:
            if xor_ret & k != 0:
                break
            k = k << 1
        # split nums into two groups, depending the k-th bit of the number
        r1, r2 = 0, 0
        for v in nums:
            if v & k == 0:
                r1 ^= v
            else:
                r2 ^= v
        return [r1 + min(min_num, 0), r2 + min(min_num, 0)]
