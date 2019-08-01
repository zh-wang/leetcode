# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        runner1 = runner2 = head
        last_runner1 = None
        while True:
            if runner2 and runner2.next and runner2.next.next:
                last_runner1 = runner1
                runner1 = runner1.next
                runner2 = runner2.next.next
            else:
                break
        root = TreeNode(runner1.val)
        if not last_runner1: # list length <= 2, runner1 == runner2 == head
            root.right = TreeNode(head.next.val) if head.next else None
        else: # head ~> last_runner1, runner1 ~> END
            last_runner1.next = None
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(runner1.next)
        return root
