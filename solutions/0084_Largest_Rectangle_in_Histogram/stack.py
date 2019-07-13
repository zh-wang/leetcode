from typing import *
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        best = 0
        temp = 0
        stack = []
        for i in range(0, len(heights)):
            if len(stack) == 0:
                stack.append(i)
            else:
                if heights[i] < heights[stack[-1]]: # found item which is descending
                    # pop until ascending order is recovered
                    while len(stack) and heights[i] < heights[stack[-1]]:
                        j = stack.pop()
                        best = max(best, (i - j) * heights[j])
                        print(best)
                stack.append(i)
            print(stack)
        if stack:
            for j in range(len(stack)):
                i = stack[j]
                if j == 0:
                    best = max(best, (stack[-1] + 1) * heights[i])
                else:
                    best = max(best, (stack[-1] - stack[j-1] + 1) * heights[i])
        return best

x = Solution().largestRectangleArea([3,2,4,8,2,9,1])
print(x)
