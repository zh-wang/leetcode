# ⭐️
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.recur(root, None)
        return root

    def recur(self, cur, tar):
        if not cur:
            return
        cur.next = tar
        self.recur(cur.left, cur.right)
        self.recur(cur.right, cur.next.left if cur.next else None)
