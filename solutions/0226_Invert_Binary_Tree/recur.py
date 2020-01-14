# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recur(root)
        return root

    def recur(self, node):
        if not node:
            return
        self.recur(node.left)
        self.recur(node.right)
        node.left, node.right = node.right, node.left
