class Solution:
    def isValid(self, s: str) -> bool:
        checker = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == '(' or c == '[' or c =='{':
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack.pop() != checker[c]:
                    return False
        return len(stack) == 0
