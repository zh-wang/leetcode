# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret = []
        self.dfs(root, 0, ret)
        return ret

    def dfs(self, node, depth, ret):
        if not node:
            return
        if depth >= len(ret):
            ret += [node.val]
        self.dfs(node.right, depth+1, ret)
        self.dfs(node.left, depth+1, ret)
