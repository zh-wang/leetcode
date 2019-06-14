class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0

        l = [0] * n
        l[0] = height[0]
        for i in range(1, n):
            l[i] = height[i] if height[i] > l[i-1] else l[i-1]

        r = [0] * n
        r[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            r[i] = height[i] if height[i] > r[i+1] else r[i+1]

        ret = 0
        for i in range(1, n-1):
            h = min(l[i-1], r[i+1])
            ret += h - height[i] if h > height[i] else 0
        return ret
