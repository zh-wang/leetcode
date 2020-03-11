# --Link--
# https://www.lintcode.com/problem/inorder-successor-in-bst/description

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return None
        if not p.right:
            # binary search node while holds p as left child
            node, p_node = root, None
            while node != p:
                if node.val < p.val:
                    node = node.right
                else:
                    p_node = node
                    node = node.left
            return p_node if p_node else None
        else:
            # find p's right child's **left most** child
            node = p.right
            while node.left:
                node = node.left
            return node
