# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        stack = []
        stack.append((root, False))
        while stack:
            node, l_visited = stack.pop()
            if node.left and not l_visited:
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                ret.append(node.val)
                if node.right:
                    stack.append((node.right, False))
        return ret
