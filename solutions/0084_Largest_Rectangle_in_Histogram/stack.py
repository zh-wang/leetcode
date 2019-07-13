class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        # Insert a dummy element to the head
        # Or a special case, 1-length stack should be handled
        heights.insert(0, 0)
        best, stack = 0, []
        for i in range(0, len(heights)):
            # found item which is descending
            if stack and heights[i] < heights[stack[-1]]:
                best = max(best, self.max_rect(heights, stack, heights[i]))
            stack.append(i)
        best = max(best, self.max_rect(heights, stack, -1))
        return best

    def max_rect(self, heights, stack, h = -1):
        """ Pop until stack's top is smaller or equals to h """
        if not stack:
            return 0
        ri, best = stack[-1], 0
        while stack and h < heights[stack[-1]]:
            hi = stack.pop()
            li = stack[-1] if stack else 0
            best = max(best, (ri - li) * heights[hi])
        return best
