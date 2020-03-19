class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        arr = str.split(' ')
        if len(arr) != len(pattern):
            return False
        dic = {}
        for i in range(len(arr)):
            a, b = pattern[i], arr[i] + '*' # modify arr to avoid the case that pattern equals to str
            if a not in dic and b not in dic:
                dic[a] = b
                dic[b] = a
            elif a in dic and dic[a] == b and b in dic and dic[b] == a:
                continue
            else:
                return False
        return True
