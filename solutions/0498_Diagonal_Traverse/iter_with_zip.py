class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        layer = m + n - 1
        r, c = 0, 0
        ret = []
        for l in range(layer):
            if l % 2 == 0: # even line
                # try move right up
                for v in zip(range(r,-1,-1), range(c,n)):
                    r, c = v[0], v[1]
                    ret += [matrix[r][c]]
                # find next start position
                if c < n-1: # try one column right
                    c += 1
                else: # otherwise, try one row down
                    r += 1
            else: # odd line
                # try move left down
                for v in zip(range(r, m), range(c,-1,-1)):
                    r, c = v[0], v[1]
                    ret += [matrix[r][c]]
                # find next start position
                if r < m-1: # try one row down first
                    r += 1
                else: # Otherwise, try one column right
                    c += 1
        return ret
