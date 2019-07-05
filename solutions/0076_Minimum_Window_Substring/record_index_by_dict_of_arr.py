from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        checker = defaultdict(int) # { char: num of char needs }
        counter = defaultdict(list) # { char: indexes of char appeared }
        for c in t:
            checker[c] += 1

        best = sys.maxsize
        ret = (-1, -1)
        match = False
        for i in range(len(s)):
            if not match:
                if s[i] in checker.keys():
                    if checker[s[i]] > 0:
                        counter[s[i]].append(i)
                        checker[s[i]] -= 1
                    else:
                        counter[s[i]].pop(0)
                        counter[s[i]].append(i)
                if not any(checker.values()): # first match
                    match = True
                    min_index = sys.maxsize
                    for index_arr in counter.values():
                        min_index = min(min_index, index_arr[0])
                    best = min(best, i - min_index + 1)
                    ret = (min_index, i)
            else: # following matches, use sliding window
                if s[i] in checker.keys():
                    counter[s[i]].pop(0)
                    counter[s[i]].append(i)
                    min_index = sys.maxsize
                    for index_arr in counter.values():
                        min_index = min(min_index, index_arr[0])
                    if i - min_index + 1 < best:
                        best = min(best, i - min_index + 1)
                        ret = (min_index, i)
        return s[ret[0]:ret[1] + 1] if ret[0] >= 0 and ret[1] >= 0 else ''
