import collections
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
        best = 1
        visited = set()
        for i in range(n):
            # all lines connecting i and j will crossing at point i
            # count slope k in hashmap
            # use faction to remove accuracy problem
            counter = collections.defaultdict(lambda: 0)
            same = 0 # count points which is equals to i
            if tuple(points[i]) in visited:
                continue
            visited.add(tuple(points[i]))
            if n-i < best:
                break
            for j in range(i+1, n):
                if points[i] == points[j]:
                    same += 1
                    continue
                if points[i][0] == points[j][0]:
                    counter["VERTICAL_LINE"] += 1
                else:
                    # a*i_0 + i_1 + c = 0
                    # a*j_0 + j_1 + c = 0
                    # a = -(i_1 - j_1) / (i_0 - j_0)
                    # c = -(i_1*j_0 - j_1*i_0) / (j_0 - i_0)
                    a_1 = points[j][1] - points[i][1]
                    a_2 = points[j][0] - points[i][0]
                    g = self.gcd(a_1, a_2)
                    counter[(a_1 // g, a_2 // g)] += 1
            best = max(best, max(counter.values() if counter else [0])+1+same)
        return best

    def gcd(self, a, b):
        return b if a % b == 0 else self.gcd(b, a % b)
