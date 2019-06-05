class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []
        wordCnt = collections.defaultdict(lambda: 0)
        for word in words:
            wordCnt[word] += 1
        k = len(words[0])
        t = len(words)
        ret = []
        for i in range(k): # sliding window start from index i
            wordMet = collections.defaultdict(lambda: 0)
            metCnt = 0
            for j in range(i, len(s), k):
                first = "" # remove this out from window
                if j-t*k >= 0:
                    first = s[j-t*k:j-(t-1)*k]
                last = s[j:j+k] # add this to window
                if first in wordCnt:
                    wordMet[first] -= 1
                if last in wordCnt:
                    wordMet[last] += 1
                if wordMet == wordCnt:
                    ret.append(j-(t-1)*k)
        return ret
