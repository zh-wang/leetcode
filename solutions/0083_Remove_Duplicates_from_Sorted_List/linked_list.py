class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        runner = head # 1, 1, 2, 2
        v = runner.val # value to check duplicated
        while runner:
            n_runner = runner.next # 1(runner), 1(n_runner), 2, 2
            while n_runner and n_runner.val == v:
                n_runner = n_runner.next # 1(runner), 1, 2(n_runner), 2
            runner.next = n_runner # 1(runner), 1(skipped) 2(n_runner), 2
            runner = runner.next # 1, 2(runner, n_runner)
            v = runner.val if runner else -1
        return head
