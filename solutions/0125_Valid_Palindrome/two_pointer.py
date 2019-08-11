class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while True:
            i, j = self.next(s, i, 1), self.next(s, j, -1)
            if i >= j:
                return True
            if self.index(s[i]) != self.index(s[j]):
                return False
            i, j = i + 1, j - 1
        return True

    def next(self, s, i, inc):
        while 0 <= i < len(s) and self.index(s[i]) < 0:
            i += inc
        return i

    def index(self, c):
        if 'a' <= c <= 'z':
            return ord(c) - 97 + 10
        elif 'A' <= c <= 'Z':
            return ord(c) - 65 + 10
        elif '0' <= c <= '9':
            return ord(c) - 48
        return -1
