# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None or t == None:
            return False
        subtree_ret = self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return subtree_ret if s.val != t.val else (subtree_ret or self.check(s, t))

    def check(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)
