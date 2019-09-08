# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        ra, rb = headA, headB
        ta, tb = None, None
        if ra == rb:
            return ra
        while True:
            if not ra.next: ta = ra
            ra = ra.next if ra.next else headB
            if not rb.next: tb = rb
            rb = rb.next if rb.next else headA
            if ta and tb and ta != tb:
                return None
            if ra == rb:
                return ra
