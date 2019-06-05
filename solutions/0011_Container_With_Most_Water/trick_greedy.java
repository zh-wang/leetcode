class Solution {
    public int maxArea(int[] height) {
        int best = 0;
        int l = 0;
        int r = height.length - 1;
        while (l < r) {
            best = Math.max(best, (r - l) * Math.min(height[r], height[l]));
            if (height[r] > height[l]) ++l;
            else --r;
        }
        return best;
    }
}
