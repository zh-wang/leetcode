# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ret = 0
        self.recur(root, False)
        return self.ret

    def recur(self, node, is_left):
        if node.left:
            self.recur(node.left, True)
        if node.right:
            self.recur(node.right, False)
        if is_left and not node.left and not node.right:
            self.ret = self.ret + node.val
