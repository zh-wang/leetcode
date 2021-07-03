# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ret = 0
        self.longestPathFromNode(root)
        return self.ret

    def longestPathFromNode(self, node):
        if not node.left and not node.right:
            return 0
        l = 0 if not node.left else (1 + self.longestPathFromNode(node.left))
        r = 0 if not node.right else (1 + self.longestPathFromNode(node.right))
        self.ret = max(l + r, self.ret)
        return max(l, r)
