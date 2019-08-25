# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        ret = []
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            if type(cur) is int:
                ret += [cur]
            else:
                stack += [cur.val]
                stack += [cur.right]
                stack += [cur.left]
        return ret
