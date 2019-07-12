# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(0) # a dummy head before real head
        new_head.next = head
        p_runner, runner = new_head, head # p_runner is parent of runner
        # p_runner -> 1 -> 1 -> 1 -> 2 -> ...
        #             ^         ^
        #           runner      |
        #                ----->runner
        while runner:
            v, cnt = runner.val, 1
            while runner.next and runner.next.val == v:
                runner = runner.next
                cnt += 1
            if cnt == 1:
                p_runner.next = runner
                p_runner = p_runner.next
                runner = p_runner.next
            else:
                p_runner.next = None
                runner = runner.next
        return new_head.next
