# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root, 0)

    def getDepth(self, node, d):
        if not node:
            return d
        return max(self.getDepth(node.left, d+1), \
                   self.getDepth(node.right, d+1))
