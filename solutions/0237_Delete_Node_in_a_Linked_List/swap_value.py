# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        while next_node:
            next_node.val, node.val = node.val, next_node.val
            if next_node.next == None:
                node.next = None
            node = next_node
            next_node = next_node.next
