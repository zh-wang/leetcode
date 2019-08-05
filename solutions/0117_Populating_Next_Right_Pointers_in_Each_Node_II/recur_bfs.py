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
        if not root:
            return None
        # Use LinkedList of cur's level to build LinkedList of next level
        head = Node(-1, None, None, None) # A dummy head of next level's LinkedList
        cur, pre = root, head
        while cur: # do for each node on cur's level
            if cur.left:
                pre.next = cur.left
                pre = pre.next
            if cur.right:
                pre.next = cur.right
                pre = pre.next
            cur = cur.next
        self.connect(head.next) # recur on next level
        return root
