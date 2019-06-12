class Solution:
    ret = []
    ret_list = []

    def letterCombinations(self, digits: str) -> List[str]:
        self.ret_list = []
        self.recur(digits, 0)
        return self.ret_list

    def recur(self, digits, depth):
        if depth == len(digits):
            if depth > 0:
                self.ret_list.append(''.join(self.ret))
            return
        r = 4 if (digits[depth] == '9' or digits[depth] == '7') else 3
        d = 1 if digits[depth] > '7' else 0
        for i in range(r):
            self.ret.append( chr(97 + (ord(digits[depth]) - 50) * 3 + d + i) )
            self.recur(digits, depth + 1)
            self.ret.pop()
