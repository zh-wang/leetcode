# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        last_runner, runner, cnt = None, head, 1
        while runner and cnt < m:
            last_runner = runner
            runner = runner.next
            cnt += 1
        rev_list_head = self.recur(runner, cnt, n, None, None)
        if not last_runner:
            head = rev_list_head
        else:
            last_runner.next = rev_list_head
        return head

    def recur(self, head, cnt, n, rev_list_head, rev_list_tail):
        if cnt > n:
            rev_list_tail.next = head
            return rev_list_head
        next_head = head.next
        head.next = rev_list_head
        if not rev_list_tail:
            rev_list_tail = head
        return self.recur(next_head, cnt+1, n, head, rev_list_tail)
