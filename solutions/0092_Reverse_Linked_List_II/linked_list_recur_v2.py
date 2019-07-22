# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        self.suc = None
        if m <= 1:
            return self.revN(head, n - m + 1)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def revN(self, head, n):
        if n == 1:
            self.suc = head.next
            return head
        last = self.revN(head.next, n - 1)
        head.next.next = head
        head.next = self.suc
        return last
