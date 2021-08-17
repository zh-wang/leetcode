class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n == 0:
            return []

        def recur(v, ret):
            if v > n:
                return
            if v != 0:
                ret += [v]
                recur(v * 10, ret)
            if v % 10 == 0:
                for i in range(1, 10):
                    recur(v + i, ret)

        ret = []
        recur(0, ret)

        return ret
