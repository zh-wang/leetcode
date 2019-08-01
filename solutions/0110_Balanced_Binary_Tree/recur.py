# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ok = True
        self.getDepth(root, 0)
        return self.ok

    def getDepth(self, root, depth):
        if not root:
            return depth
        l = self.getDepth(root.left, depth+1)
        r = self.getDepth(root.right, depth+1)
        if abs(l - r) > 1:
            self.ok = False
        return max(l, r)
