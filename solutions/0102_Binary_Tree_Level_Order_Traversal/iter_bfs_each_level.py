# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        l = []
        l += [root]
        while l:
            new_ret = []
            new_l = []
            for node in l:
                new_ret += [node.val]
                if node.left:
                    new_l += [node.left]
                if node.right:
                    new_l += [node.right]
            l = new_l
            ret += [new_ret]
        return ret
