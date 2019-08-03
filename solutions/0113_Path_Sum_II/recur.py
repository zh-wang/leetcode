# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.ret = []
        self.check(root, sum, [])
        return self.ret

    def check(self, root, sum, l):
        if not root.left and not root.right:
            if sum == root.val:
                l += [root.val]
                self.ret += [l]
        elif not root.left:
            self.check(root.right, sum - root.val, l + [root.val])
        elif not root.right:
            self.check(root.left, sum - root.val, l + [root.val])
        else:
            self.check(root.left, sum - root.val, l + [root.val])
            self.check(root.right, sum - root.val, l + [root.val])
