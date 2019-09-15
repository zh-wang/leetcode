class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ''
        while n > 0:
            ret += chr((n-1)%26 + 65)
            n = (n-1) // 26 # -1 is the mvp
        return ret[::-1]
