/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(0);
        ListNode r1 = less;
        ListNode more = new ListNode(0);
        ListNode r2 = more;
        while (head != null) {
            boolean isLess = false;
            if (head.val < x) {
                r1.next = head;
                r1 = r1.next;
                isLess = true;
            } else {
                r2.next = head;
                r2 = r2.next;
                isLess = false;
            }
            head = head.next;
            if (isLess) r1.next = null;
            else r2.next = null;
        }
        // merge two lists
        ListNode newHead;
        if (less.next != null) {
            r1.next = more.next;
            newHead = less.next;
        } else {
            newHead = more.next;
        }
        return newHead;
    }
}
