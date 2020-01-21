# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        self.snapshot_p = []
        self.snapshot_q = []
        self.dfs(root, p, q, stack)
        ret = None
        for i in range(min(len(self.snapshot_p), len(self.snapshot_q))):
            if self.snapshot_p[i] == self.snapshot_q[i]:
                ret = self.snapshot_p[i]
            else:
                break
        return ret

    def dfs(self, node, p, q, stack):
        if not node:
            return
        stack += [node]
        if node.val == p.val:
            self.snapshot_p = stack[:]
        if node.val == q.val:
            self.snapshot_q = stack[:]
        self.dfs(node.left, p, q, stack)
        self.dfs(node.right, p, q, stack)
        stack.pop()
