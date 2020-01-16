# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ret = None
        self.count(root, 0, k)
        return self.ret

    # count # of nodes in this subtree
    # t: start index
    # k: target index
    def count(self, node, t, k):
        if not node:
            return 0
        l = self.count(node.left, t, k)
        # (start index for right subtree) = (current start index) + (# of nodes in left tree) + 1
        r = self.count(node.right, t + l + 1, k)
        if l + t == k - 1:
            self.ret = node.val
        return l + r + 1
