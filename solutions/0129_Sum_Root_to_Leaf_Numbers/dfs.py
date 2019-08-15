# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ret = 0
        self.dfs(root, 0)
        return self.ret

    def dfs(self, root, num):
        nextVal = num*10+root.val
        if not root.left and not root.right:
            self.ret += nextVal
        elif not root.left:
            self.dfs(root.right, nextVal)
        elif not root.right:
            self.dfs(root.left, nextVal)
        else:
            self.dfs(root.left, nextVal)
            self.dfs(root.right, nextVal)
