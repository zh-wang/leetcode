class Solution:
    def trap(self, height: List[int]) -> int:
        ret, i, n = 0, 0, len(height)
        stack = []
        while i < n:
            while len(stack) and height[i] > height[stack[-1]]:
                bi = stack.pop() # bottom's index
                if (len(stack) == 0):
                    break
                d = i - stack[-1] - 1
                ret += (min(height[i], height[stack[-1]]) - height[bi]) * d
            stack.append(i)
            i += 1
        return ret
