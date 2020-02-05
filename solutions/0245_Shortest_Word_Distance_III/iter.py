# --Link--
# http://www.learn4master.com/interview-questions/leetcode/leetcode-shortest-word-distance-i-ii-and-iii

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        if None == word1 or None == word2:
            return -1
        best = len(words)
        if word1 != word2:
            p1, p2 = -len(words), -len(words)
            for i, w in enumerate(words):
                if w == word1:
                    p1 = i
                    best = min(best, p1 - p2)
                if w == word2:
                    p2 = i
                    best = min(best, p2 - p1)
        else:
            p = -len(words)
            for i, w in enumerate(words):
                if w == word1:
                    best = min(best, i - p)
                    p = i
        return best if best < len(words) else -1

words = ['a', 'b', 'c', 'b', 'a', 'b', 'g', 'g', 'k']
print( Solution().shortestDistance(words, 'a', 'c') )
print( Solution().shortestDistance(words, 'b', 'c') )
print( Solution().shortestDistance(words, 'g', 'c') )
print( Solution().shortestDistance(words, 'c', 'c') )
print( Solution().shortestDistance(words, 'a', 'a') )
print( Solution().shortestDistance(words, 'g', 'g') )
print( Solution().shortestDistance(words, 'b', 'b') )
