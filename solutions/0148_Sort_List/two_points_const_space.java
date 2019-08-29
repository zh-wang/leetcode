/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null) return null;
        ListNode slow = head;
        ListNode fast = head;
        // 1->2->3   ===>   1->2, 3
        // 1->2      ===>   1, 2
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        if (fast.next != null) fast = fast.next;

        if (slow == fast) {
            return slow;
        }

        ListNode head2 = slow.next;
        slow.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(head2); // maybe empty
        return mergeTwoListsInPlace(h1, h2);
    }

    private ListNode mergeTwoListsInPlace(ListNode h1, ListNode h2) {
        ListNode r1 = h1;
        ListNode r2 = h2;
        ListNode dummy = new ListNode(-1);
        ListNode r3 = dummy;
        while (r1 != null && r2 != null) {
            if (r1.val < r2.val) {
                r3.next = r1; // r3->r1
                r1 = r1.next; // update r1
                r3 = r3.next; // move r3 to r1
            } else {
                r3.next = r2;
                r2 = r2.next;
                r3 = r3.next;
            }
        }
        if (r1 == null) r3.next = r2;
        if (r2 == null) r3.next = r1;
        return dummy.next;
    }
}
