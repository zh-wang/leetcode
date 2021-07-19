class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(',')
        # turn leaf node into #
        # e.g. 3,#,# can be turned into #
        stack = []
        for i in range(len(arr)):
            v = arr[i]
            stack += [v]
            while len(stack) > 1 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                stack[-1] = '#'
        return stack == ['#']
