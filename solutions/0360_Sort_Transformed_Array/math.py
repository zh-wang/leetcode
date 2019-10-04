class Solution:
    """
    @param nums: a sorted array
    @param a:
    @param b:
    @param c:
    @return: a sorted array
    """
    def sortTransformedArray(self, nums, a, b, c):
        # Write your code here
        if a == 0:
            ret = [b*v + c for v in nums]
            return ret if b >= 0 else list(reversed(ret))
        center = -b/a/2
        dist = sorted(nums, key=lambda v: abs(v - center))
        ret = [a*v*v + b*v + c for v in dist]
        return ret if a > 0 else list(reversed(ret))
