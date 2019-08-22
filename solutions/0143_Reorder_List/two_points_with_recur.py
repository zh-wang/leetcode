# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow = fast = head
        while True: # find the middle node
            if not fast.next or not fast.next.next:
                break
            fast = fast.next.next
            slow = slow.next
        head_1 = head # first half of linked list
        head_2 = self.rev(slow.next, None)[0] if slow.next else None # second half
        slow.next = None
        # build result with above two halves
        dummy = runner = ListNode(0)
        while head_2:
            runner.next = head_1 # order matters!!!
            head_1 = head_1.next
            runner = runner.next # runner at head_1
            runner.next = head_2 # point head_1's next to head_2
            head_2 = head_2.next
            runner = runner.next # runner at head_2
        if head_1: # first half may have 1 additional node
            runner.next = head_1
            head_1.next = None
        return dummy.next

    def rev(self, head, tail):
        if not head.next:
            return (head, head)
        c_head, c_tail = self.rev(head.next, tail)
        c_tail.next = head
        head.next = None
        return (c_head, head)

