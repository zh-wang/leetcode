from typing import *

class Solution:

    pos_map = {}

    def decodeString(self, s: str) -> str:
        if not self.pos_map:
            self.pos_map = {}
            stack = []
            for (i, c) in enumerate(s):
                if c == '[':
                    stack += [i]
                if c == ']':
                    self.pos_map[stack.pop()] = i
            return self.recur(s, 0, len(s)-1)

    def recur(self, s, l, r):
        ret, cnt, i = '', 0, l
        while i <= r:
            if s[i] == '[':
                ret = ret + cnt * self.recur(s, i+1, self.pos_map[i]-1)
                cnt, i = 0, self.pos_map[i] + 1
                continue
            elif s[i].isdigit():
                cnt = cnt * 10 + int(s[i])
            else:
                ret = ret + s[i]
            i += 1
        return ret

x = Solution().decodeString("aa2[b5[c]dd]e")
print(x)
