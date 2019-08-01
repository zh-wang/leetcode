# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)
        num_left = root_index
        num_right = len(inorder) - 1 - root_index
        l_pre = preorder[1:num_left+1]
        r_pre = preorder[num_left+1:]
        l_in = inorder[:num_left]
        r_in = inorder[num_left+1:]
        root.left = self.buildTree(l_pre, l_in)
        root.right = self.buildTree(r_pre, r_in)
        return root
