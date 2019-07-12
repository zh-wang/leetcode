class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        runner = head
        v = runner.val
        while runner:
            n_runner = runner.next
            while n_runner and n_runner.val == v:
                n_runner = n_runner.next
            runner.next = n_runner
            runner = runner.next
            v = runner.val if runner else -1
        return head
