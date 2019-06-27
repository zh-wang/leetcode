class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return []

        runner, n = head, 0 # get the length of list
        while runner != None:
            n += 1
            runner = runner.next

        k %= n # if k > n, get mod of n
        if k == 0:
            return head

        start, runner = head, head
        while k > 0:
            runner = runner.next
            k -= 1
        while runner.next != None:
            runner, start = runner.next, start.next
        newhead = start.next
        runner.next = head
        start.next = None
        return newhead
