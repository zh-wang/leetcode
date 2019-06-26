class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0 for _ in range(n)] for _ in range(n)]
        v = 1
        l = 0
        while l < (n+1) // 2:
            r1, r2, c1, c2 = l, n-1-l, l, n-1-l
            for i in range(c1, c2+1, 1):
                ret[r1][i] = v
                v += 1
            for i in range(r1+1, r2+1, 1):
                ret[i][c2] = v
                v += 1
            if c2 > c1:
                for i in range(c2-1, c1-1, -1):
                    ret[r2][i] = v
                    v += 1
            if r2 > r1:
                for i in range(r2-1, r1, -1):
                    ret[i][c1] = v
                    v += 1
            l += 1
        return ret
