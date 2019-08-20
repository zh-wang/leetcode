# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        runner = head
        while runner:
            if runner in visited:
                return True
            visited.add(runner)
            runner = runner.next
        return False
