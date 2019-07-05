from collections import defaultdict
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count = defaultdict(int) # { char: num of char needs }
        char_met = defaultdict(int)
        for c in t:
            char_count[c] += 1

        # chars contains valid characters
        # indexes contains the index of each char in chars
        chars, indexes = [], []
        for i in range(len(s)):
            if s[i] in char_count.keys():
                chars.append(s[i])
                indexes.append(i)

        i, j = 0, 0
        best, ret = sys.maxsize, (-1, -1)
        num_of_met = 0
        for i in range(len(indexes)):
            char_met[chars[i]] += 1
            if char_met[chars[i]] == char_count[chars[i]]:
                num_of_met += 1
            # Each time we found a valid (i, j),
            # we remove j out of the window one by one,
            # until (i, j) becomes invalid.
            while num_of_met == len(char_count): # is valid?
                t = indexes[i] - indexes[j] + 1
                if t < best:
                    best = t
                    ret = (indexes[j], indexes[i])
                if char_met[chars[j]] == char_count[chars[j]]:
                    num_of_met -= 1
                char_met[chars[j]] -= 1
                j += 1

        return s[ret[0]:ret[1]+1] if ret[0] >= 0 and ret[1] >= 0 else ''
