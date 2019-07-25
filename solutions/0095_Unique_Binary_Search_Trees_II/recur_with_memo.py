# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dp = [[ [] for _ in range(n+1) ] for _ in range(n+1)]
        return self.recur(dp, 1, n)

    def recur(self, dp, i, j):
        if i > j:
            return [None]
        if dp[i][j]:
            return dp[i][j]
        if i == j:
            dp[i][j] = [TreeNode(i)]
            return dp[i][j]
        else:
            for k in range(i, j+1):
                for lc in self.recur(dp, i, k-1):
                    for rc in self.recur(dp, k+1, j):
                        node = TreeNode(k)
                        node.left, node.right = lc, rc
                        dp[i][j].append(node)
            return dp[i][j]

