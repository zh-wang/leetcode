# STAR

from typing import *
from functools import reduce

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyList = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: # inc pair from left to right
                candyList[i] = max(candyList[i], candyList[i - 1] + 1)

        for i in range(len(ratings) - 2, -1, -1): # inc pair from right to left
            if ratings[i] > ratings[i + 1]:
                candyList[i] = max(candyList[i], candyList[i + 1] + 1)

        return reduce(lambda x, y: x + y, candyList)

# #                     2, 1, 2, 1, 2, 3, 4, 1, 2
# x = Solution().candy([1, 0, 1, 1, 2, 3, 4, 0, 2])
# print(x)
# #                 1,2,1
# x = Solution().candy([1,2,2])
# print(x)
# #                 1,2,1,2,1
# x = Solution().candy([1,3,2,2,1])
# print(x)
