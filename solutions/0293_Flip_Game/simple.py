# --Link--
# https://www.lintcode.com/problem/flip-game/description

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        ret = []
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                ret += [s[:i] + '--' + s[i+2:]]
        return ret
