# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret = -1<<32
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        cur_sum = root.val + max(0, l) + max(0, r)
        self.ret = max(self.ret, cur_sum)
        return max(0, root.val + max(0, l, r))
