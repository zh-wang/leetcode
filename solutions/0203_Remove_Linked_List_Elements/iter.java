/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode runner = head;
        ListNode pRunner = dummy;
        while (runner != null) {
            if (runner.val == val) {
                pRunner.next = runner.next;
            } else {
                pRunner = pRunner.next;
            }
            runner = runner.next;
        }
        return dummy.next;
    }
}
