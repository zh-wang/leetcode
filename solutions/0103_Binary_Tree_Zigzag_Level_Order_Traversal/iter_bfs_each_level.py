# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import reduce
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret, l = [], []
        l += [root]
        reverse_order = 0
        while l:
            new_ret, new_l = [], []
            for node in l:
                new_ret += [node.val]
                if node.left:
                    new_l += [node.left]
                if node.right:
                    new_l += [node.right]
            l = new_l
            ret += [list(reversed(new_ret))] if reverse_order else [new_ret]
            reverse_order = 1 - reverse_order
        return ret
