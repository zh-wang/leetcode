from functools import reduce

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        arrSum = sum(A)
        rotateSum = sum([A[i] * i for i in range(len(A))])
        best = rotateSum
        temp = rotateSum
        for i in range(1, len(A)):
            temp = temp + arrSum - len(A) * A[len(A) - i]
            best = max(best, temp)
        return best
