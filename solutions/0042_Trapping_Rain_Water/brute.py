class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        ret = 0
        for i in range(1, len(height) - 1):
            h = min(max(height[:i]), max(height[i+1:]))
            ret += h - height[i] if h > height[i] else 0
        return ret
