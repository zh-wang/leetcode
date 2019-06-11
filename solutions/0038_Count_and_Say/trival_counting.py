class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(1, n):
            ss = ''
            j, cnt = 0, 0
            target = ''
            while j < len(s):
                if (cnt == 0):
                    target, cnt = s[j], 1
                    j += 1
                else:
                    while j < len(s) and target == s[j]:
                        j, cnt = j + 1, cnt + 1
                    ss += str(cnt)
                    ss += target
                    target, cnt = '', 0
            if cnt > 0:
                ss += str(cnt)
                ss += target
            s = ss
        return s
