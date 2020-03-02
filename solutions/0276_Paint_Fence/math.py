class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        # r1 => # of different color combinations in last two fences
        # r2 => # of same color combinations in last two fences
        r1, r2 = k, 0
        for i in range(1, n):
            # for r1
            next_r2 = r1
            next_r1 = r1 * (k - 1)
            # for r2
            next_r1 += r2 * (k - 1)
            r1, r2 = next_r1, next_r2
        return r1 + r2
