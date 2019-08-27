/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode target = head;
        ListNode pTarget = dummy;
        while (target != null) {
            ListNode runner = dummy.next;
            ListNode pRunner = dummy;
            ListNode nTarget = target.next; // keep target's next, because target may change position
            while (runner != target && target.val > runner.val) {
                pRunner = runner;
                runner = runner.next;
            }
            if (runner != target) { // if changing position occurs
                pTarget.next = target.next; // cut target
                pRunner.next = target; // link runner's prev and target
                target.next = runner; // link target and runner
                target = nTarget; // ** make nTarget as target, no change for pTarget **
            } else { // if no changing position occurs
                pTarget = target; // make both to their next
                target = nTarget;
            }
        }
        return dummy.next;
    }
}
