# --Link--
# https://www.lintcode.com/problem/flip-game-ii/description

class Solution:

    checked = {}

    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        # write your code here
        if '++' not in s:
            return False
        if s in self.checked:
            return self.checked[s]
        ret = True
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                ret = ret and self.canWin(s[:i] + '--' + s[i+2:])
        self.checked[s] = not ret
        return self.checked[s]
