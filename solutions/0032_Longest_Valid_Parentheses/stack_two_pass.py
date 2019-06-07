class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        pairs = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif len(stack) > 0:
                j = stack.pop()
                pairs.append([j, i])
        pairs = sorted(pairs, key=lambda p: p[0])
        if len(pairs) == 0: return 0
        best = 0
        temp, r = pairs[0][1] - pairs[0][0] + 1, pairs[0][1]
        for p in pairs:
            if p[0] == r + 1:
                temp += (p[1] - p[0] + 1)
                r = p[1]
            elif p[0] > r + 1:
                best = max(best, temp)
                temp, r = p[1] - p[0] + 1, p[1]
        best = max(best, temp)
        return best
