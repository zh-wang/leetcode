class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.temp = []
        self.ret = []
        self.recur(s, 0, 0)
        return self.ret

    def recur(self, s, i, d):
        if d >= 4:
            if i == len(s):
                self.ret.append('.'.join(self.temp))
            return
        if i+1<=len(s) and '0'<=s[i:i+1]<='9':
            self.temp.append(s[i])
            self.recur(s, i+1, d+1)
            self.temp.pop()
        if i+2<=len(s) and '10'<=s[i:i+2]<='99':
            self.temp.append(s[i:i+2])
            self.recur(s, i+2, d+1)
            self.temp.pop()
        if i+3<=len(s) and '100'<=s[i:i+3]<='255':
            self.temp.append(s[i:i+3])
            self.recur(s, i+3, d+1)
            self.temp.pop()
