# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        r1, r2 = head, head
        while r2.next and r2.next.next: # r1 will be the center point
            r1 = r1.next
            r2 = r2.next.next
        rev = ListNode(-1) # reverse from r1.next
        r3 = r1.next
        while r3:
            next_r3 = r3.next # r3.next will be modified, so keep it
            r3.next = rev.next
            rev.next = r3
            r3 = next_r3
        r1, r2 = head, rev.next # compare from head and rev.next simutaniously
        while r1 and r2:
            if r1.val != r2.val:
                return False
            r1, r2 = r1.next, r2.next
        return True
