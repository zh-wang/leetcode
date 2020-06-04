class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        # let k to be 2's exponential growth
        # 00000 = 0 2**0
        # 00001 = 1 < 2**1 - 1
        # 00010 = 1
        # 00011 = 2 << 2**2 - 1
        # 00100 = 1
        # 00101 = 2
        # 00110 = 2
        # 00111 = 3 <<< 2**3 - 1
        # 01000 = 1
        # 01001 = 2
        # 01010 = 2
        # 01011 = 3
        # 01100 = 2
        # 01101 = 3
        # 01110 = 3
        # 01111 = 4 <<<< 2**4 - 1
        # 10000 = 1
        if num == 0:
            return [0]
        ret = [0]
        k = 1
        while len(ret) < num + 1:
            ret += [v + 1 for v in ret]
            k += 1
        return ret[:num + 1]
