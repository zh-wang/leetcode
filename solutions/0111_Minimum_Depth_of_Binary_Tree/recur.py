# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.getDepth(root, 1)

    def getDepth(self, root, depth):
        if not root.left and not root.right:
            return depth
        elif not root.left:
            return self.getDepth(root.right, depth + 1)
        elif not root.right:
            return self.getDepth(root.left, depth + 1)
        else:
            return min(self.getDepth(root.left, depth + 1), \
                       self.getDepth(root.right, depth + 1))
