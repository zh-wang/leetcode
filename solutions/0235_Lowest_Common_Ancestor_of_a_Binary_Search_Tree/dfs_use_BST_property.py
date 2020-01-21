# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s1 = []
        s2 = []
        self.dfs(root, p, [root], s1)
        self.dfs(root, q, [root], s2)
        ret = None
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                ret = s1[i]
            else:
                break
        return ret

    def dfs(self, node, v, stack, path):
        if not node:
            return
        if node.val == v.val:
            path += stack[:]
            return
        if node.val < v.val:
            self.dfs(node.right, v, stack + [node.right], path)
        else:
            self.dfs(node.left, v, stack + [node.left], path)
