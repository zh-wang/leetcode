# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        e1, e2 = None, None
        lastNode = None
        for node in self.inorder(root):
            if not lastNode:
                lastNode = node
            else:
                if not e1:
                    if lastNode.val > node.val:
                        e1 = lastNode
                        e2 = node
                else:
                    if lastNode.val > node.val:
                        e2 = node
                lastNode = node
        e1.val, e2.val = e2.val, e1.val

    def inorder(self, node):
        if not node:
            return 
        for k in self.inorder(node.left):
            yield k
        yield node
        for k in self.inorder(node.right):
            yield k
