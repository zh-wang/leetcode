# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh, rh = 0, 0
        runner = root
        while runner:
            runner = runner.left
            lh += 1
        runner = root
        while runner:
            runner = runner.right
            rh += 1
        if lh == rh:
            return (1 << lh) - 1
        return (1 << (lh - 1)) - 1 + \
            self.recur(root, lh, 1, 1 << (lh - 1))

    # last level
    # 1, 2, 3, 4
    #    l  r
    def recur(self, node, h, l, r):
        if l == r:
            return l
        lnode, lh = node.left, h - 1
        while lnode:
            lnode, lh = lnode.right, lh - 1
        rnode, rh = node.right, h - 1
        while rnode:
            rnode, rh = rnode.left, rh - 1
        mid = (l + r) // 2
        if lh == 0 and rh == 0: # l and r both exist, we can search the right part
            return self.recur(node.right, h - 1, mid + 1, r)
        elif lh == 0: # l exists but r is not, no need to search the right part
            return mid
        else: # l doesn't exist, search the left part
            return self.recur(node.left, h - 1, l, mid)
