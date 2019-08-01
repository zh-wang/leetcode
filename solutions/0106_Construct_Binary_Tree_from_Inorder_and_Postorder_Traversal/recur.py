# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.buildTree(inorder, postorder)

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root_val = postorder[-1]
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)
        num_left = root_index
        num_right = len(inorder) - 1 - root_index
        l_post = postorder[:num_left]
        r_post = postorder[num_left:-1]
        l_in = inorder[:num_left]
        r_in = inorder[num_left+1:]
        root.left = self.buildTree(l_in, l_post)
        root.right = self.buildTree(r_in, r_post)
        return root

