import collections

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        arr = str.split(' ')
        if len(arr) != len(pattern):
            return False
        d1, d2 = collections.defaultdict(lambda: ''), collections.defaultdict(lambda: '')
        for i in range(len(arr)):
            if pattern[i] not in d1 and arr[i] not in d2:
                d1[pattern[i]] = arr[i]
                d2[arr[i]] = pattern[i]
            elif d1[pattern[i]] != arr[i] or d2[arr[i]] != pattern[i]:
                return False
        return True
