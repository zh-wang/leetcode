# --Link--
# https://www.lintcode.com/problem/shortest-word-distance/description

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        best = len(words)
        p1, p2 = -len(words), -len(words)
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
                best = min(best, p1 - p2)
            if w == word2:
                p2 = i
                best = min(best, p2 - p1)
        return best
