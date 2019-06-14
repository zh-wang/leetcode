/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode runner = head;
        while (n - 1 > 0) {
            runner = runner.next;
            --n;
        }
        if (runner.next == null) return head.next;
        ListNode target = head;
        ListNode target_p = null;
        while (runner.next != null) {
            target_p = target;
            target = target.next;
            runner = runner.next;
        }
        target_p.next = target.next;
        return head;
    }
}
