class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ret = m
        bitmax, _n = 0, n
        while _n > 0:
            bitmax, _n = bitmax + 1, _n >> 1

        # go from the rightmost bit
        i = bitmax - 1
        while i >= 0:
            # if we found a 1-bit will be flip to 0,
            # all bits right to it and itself will be 0
            # we can skip remaining checks
            if (ret >> i) & 1:
                j = i
                while j >= 0 and (ret >> j) & 1: # find consecusive 1s
                    j -= 1 # j is the next i to search from
                # flip (i+1)th bit to 1, all bits on the right to 0
                checker = ((ret >> i+1) + 1) << i+1
                if checker <= n:
                    ret = ret & checker
                    break
                i = j
            else:
                i -= 1
        return ret
