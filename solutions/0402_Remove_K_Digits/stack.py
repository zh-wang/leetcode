from typing import *
import re

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # user filter to remove empty group which may appear at the end
        groups = list( filter(lambda a: a, re.split('([0]+)', num)) )
        for i in range(len(groups)):
            if k > 0:
                if groups[i][0] != '0':
                    x = self.removeInGroup(groups[i], k)
                    k -= len(groups[i])
                    groups[i] = x
                else:
                    groups[i] = ''

        groups = list( filter(lambda a: a, groups) )
        if groups and groups[0][0] == '0':
            del groups[0]

        ret = ''.join(groups)
        return '0' if not ret else ret

    def removeInGroup(self, s, k):
        if k >= len(s): # k is too large, we can remove all digits from s
            return ''
        stack = []
        for c in s:
            if not stack:
                stack += [c]
            else:
                while stack and stack[-1] > c and k > 0:
                    stack.pop()
                    k -= 1
                stack += [c]
        if k > 0:
            stack = stack[:len(stack) - k]
        return ''.join(stack)
