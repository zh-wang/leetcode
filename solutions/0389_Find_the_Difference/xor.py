from functools import reduce

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr( reduce(lambda x, y: x ^ ord(y), list(s + t), 0) )
