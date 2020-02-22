# --Link--
# https://www.lintcode.com/problem/palindrome-permutation/description

from collections import defaultdict

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        numOfOne = [val for val in counts.values() if val % 2 == 1]
        return len(numOfOne) <= 1
