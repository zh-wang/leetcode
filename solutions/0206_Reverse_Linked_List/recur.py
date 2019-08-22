# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.rev(head, None)[0]

    def rev(self, head, tail):
        if not head.next:
            return (head, head)
        c_head, c_tail = self.rev(head.next, tail)
        c_tail.next = head
        head.next = None
        return (c_head, head)
