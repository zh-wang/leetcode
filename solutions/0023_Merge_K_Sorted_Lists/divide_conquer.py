# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not len(lists): return []
        return self.mergeKListsDK(lists, 0, len(lists) - 1)

    def mergeKListsDK(self, lists, l, r):
        if l == r:
            return lists[l]
        m = (l + r) // 2
        a = self.mergeKListsDK(lists, l, m)
        b = self.mergeKListsDK(lists, m + 1, r)
        return self.merge2list(a, b)

    def merge2list(self, a, b):
        head = ListNode(0)
        runner = head
        while a and b:
            if a.val < b.val:
                runner.next = a
                a = a.next
            else:
                runner.next = b
                b = b.next
            runner = runner.next
        if not a:
            runner.next = b
        else:
            runner.next = a
        return head.next
