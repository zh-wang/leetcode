class Solution {
    int best = 0;

    public int largestRectangleArea(int[] heights) {
        best = 0;
        int n = heights.length;
        // Insert a dummy element to the head
        // Or a special case in recur should be handled
        int[] heights2 = new int[n + 1];
        heights2[0] = 0;
        for (int i = 1; i < n+1; ++i) heights2[i] = heights[i-1];
        recur(heights2, n+1, 0, 0, heights2[0]);
        return best;
    }

    // This method tracks an ascending level, like [2,2,3] or [2,3]
    // l and r points to the stack and end of that level
    // h is the height of the end
    private int recur(int[] heights, int n, int l, int r, int h) {
        int tmp = 0;
        while (true) {
            if (r < n && h == heights[r]) { // found an equal height
                tmp = ++r;
            } else if (r < n && h < heights[r]) { // found a taller height
                r = recur(heights, n, tmp, r, heights[r]);
            } else if (r == n || h > heights[r]) { // found a value descending or the end of hist
                best = Math.max(best, (r - l) * h);
                return r;
            }
        }
    }
}
