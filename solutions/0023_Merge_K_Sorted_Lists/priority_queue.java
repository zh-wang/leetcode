/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> q = new PriorityQueue<>((a, b) -> {
            return a.val - b.val;
        });
        for (ListNode node : lists) {
            if (node != null) q.add(node);
        }
        ListNode head = new ListNode(0);
        ListNode runner = head;
        while (!q.isEmpty()) {
            ListNode node = q.poll();
            runner.next = node;
            if (node.next != null) {
                q.add(node.next);
            }
            runner = runner.next;
        }
        return head.next;
    }
}
