"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j:
                    if Celebrity.knows(i, j):
                        break
                    if Celebrity.knows(j, i):
                        cnt += 1
            if cnt == n - 1:
                return i
        return -1
