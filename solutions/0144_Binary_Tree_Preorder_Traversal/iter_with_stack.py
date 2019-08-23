# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            ret += [node.val]
            if node.right:
                stack += [node.right]
            if node.left:
                stack += [node.left]
        return ret
