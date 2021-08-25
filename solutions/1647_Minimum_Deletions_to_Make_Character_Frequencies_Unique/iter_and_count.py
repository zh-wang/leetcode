class Solution:
    def minDeletions(self, s: str) -> int:
        # frequency of each char
        char_counter = Counter([c for c in s])
        # count number of each frequency
        uniq_freq = [0] * (max(char_counter.values()) + 1)
        for v in char_counter.values():
            uniq_freq[v] += 1

        ret = 0
        # go from largest frequency
        i = len(uniq_freq) - 1
        while i > 0:
            if uniq_freq[i] > 1:
                uniq_freq[i - 1] += (uniq_freq[i] - 1)
                ret += (uniq_freq[i] - 1)
            i -= 1
        return ret
