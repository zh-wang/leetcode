# STAR

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while True:
            while node:
                stack += [node]
                node = node.left
            if not stack:
                break
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return 0
