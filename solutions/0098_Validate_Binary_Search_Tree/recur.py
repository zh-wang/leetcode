# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.ret = True
        self.recur(root)
        return self.ret

    def recur(self, node):
        lmin, lmax = self.recur(node.left) if node.left else (float('inf'),float('-inf'))
        rmin, rmax = self.recur(node.right) if node.right else (float('inf'),float('-inf'))
        if node.val <= lmax:
            self.ret = False
        if node.val >= rmin:
            self.ret = False
        return (min(lmin, rmin, node.val), max(lmax, rmax, node.val))
