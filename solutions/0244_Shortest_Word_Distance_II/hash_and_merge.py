# --Link--
# http://www.learn4master.com/interview-questions/leetcode/leetcode-shortest-word-distance-i-ii-and-iii

from collections import defaultdict

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        pos = defaultdict(lambda: [])
        for i, w in enumerate(words):
            pos[w] += [i]
        return self.distance(pos[word1], pos[word2])

    def distance(self, pa, pb):
        if not pa or not pb:
            return -1
        i, j = 0, 0
        best = 1 << 32
        while i < len(pa) and j < len(pb):
            best = min(abs(pa[i] - pb[j]), best)
            if pa[i] > pb[j]:
                j += 1
            else:
                i += 1
        return best

words = ['a', 'b', 'c', 'b', 'a', 'b', 'g', 'g', 'k']
print( Solution().shortestDistance(words, 'a', 'c') )
print( Solution().shortestDistance(words, 'b', 'c') )
print( Solution().shortestDistance(words, 'g', 'c') )
