import collections

class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """

    def balanceGraph(self, edges):
        # Write your code here
        weights = collections.defaultdict(int) # point => final weight
        for e in edges:
            weights[e[0]] -= e[2]
            weights[e[1]] += e[2]

        arr = [] # contains non-zero weights
        for w in weights.values():
            if w != 0:
                arr += [w]

        dp = collections.defaultdict(int)
        return self.dfs(0, 0, arr)

    def dfs(self, start, steps, arr):
        ret = 1 << 32
        while start < len(arr) and arr[start] == 0:
            start += 1
        # for arr[start] and arr[i],
        # let arr[start] to be 0, arr[i] += arr[start]
        # this means a weighted edge (arr[i], arr[start], arr[start]) is added
        for i in range(start + 1, len(arr)):
            if arr[i] * arr[start] < 0:
                arr[i] += arr[start]
                # arr[start] is 0, so we start from start + 1
                ret = min(ret, self.dfs(start + 1, steps + 1, arr))
                arr[i] -= arr[start]
        return ret if ret < (1 << 32) else steps
