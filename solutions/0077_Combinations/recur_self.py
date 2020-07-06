class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combine(n, k) = combine(n-1, i-1) + [i],      k <= i <= n
        # 1. For the element we pick for combine(n, k),
        # we can pick it from k to n, cause we need at least k elements to form the answer.
        # (We know that the first, or minimal in sequence order, is 1, 2, ..., k)
        # 2. After picker i, the problem falls down to a sub-problem combine(i-1, k-1),
        # mean that we need to choose k-1 elements from i-1 values.
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
