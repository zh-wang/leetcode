# --Link--
# https://www.lintcode.com/problem/strobogrammatic-number/description

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        n = len(num)
        for i in range(n // 2 + 1):
            if num[i] == '1' and num[n - 1 - i] == '1' or \
                num[i] == '0' and num[n - 1 - i] == '0' or \
                num[i] == '6' and num[n - 1 - i] == '9' or \
                num[i] == '8' and num[n - 1 - i] == '8' or \
                num[i] == '9' and num[n - 1 - i] == '6':
                    continue
            else:
                return False
        return True
