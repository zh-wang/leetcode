// ⭐️
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b0, b1 = 0, 0
        for k in nums:
            b0 = (b0 ^ k) & ~b1
            b1 = (b1 ^ k) & ~b0
        return b0

#   i0  i1  k  i0' i1'
#   0   0   0   0   0   s0
#   0   1   0   0   1   s1
#   1   0   0   1   0   s2
#   1   1   0   1   x
#   0   0   1   0   1   s0 => s1
#   0   1   1   1   0   s1 => s2
#   1   0   1   0   0   s2 => s0
#   1   1   1   0   x
# i0' = (i0 & ~i1 & ~k) | (~i0 & i1 & k)
# i1' = (~i0 & i1 & ~k) | (~i0 & ~i1 & k)

# Above truth table need two additional variable i0' & i1'.
# Instead, we can use i0 & i1 directly and make it simplier by modifing the truth table.

#   i0  i1  k  i0' i1'
#   0   0   0   0   0   s0
#   0   1   0   0   1   s2
#   1   0   0   1   0   s1
#   1   1   0   1   x
#   0   0   1   1   0   s0 => s1
#   0   1   1   0   0   s2 => s0
#   1   0   1   0   1   s1 => s2
#   1   1   1   0   x
#
#   i0' = (i0 & ~i1 & ~k) | (~i0 & ~i1 & k) = ~i1 & (i0 ^ k)
#   i1' = (~i0' & i1 & ~k) | (~i0' & ~i1 & k) = ~i0' & (i1 ^ k)
#
#   By above modification, i1' is calculated by i0' instead of i0, resulting a simplier implementation.
