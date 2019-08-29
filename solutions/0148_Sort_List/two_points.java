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
        while (true) {
            if (fast.next != null) fast = fast.next;
            else break;
            if (fast.next != null) fast = fast.next;
            else break;
            slow = slow.next;
        }

        if (slow == fast) {
            return slow;
        }

        ListNode head2 = slow.next;
        slow.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(head2); // maybe empty
        return mergeTwoLists(h1, h2);
    }

    private ListNode mergeTwoLists(ListNode h1, ListNode h2) {
        if (h2 == null) return h1;
        if (h1 == null) return h2;
        if (h1.val < h2.val) {
            h1.next = mergeTwoLists(h1.next, h2);
            return h1;
        } else {
            h2.next = mergeTwoLists(h1, h2.next);
            return h2;
        }
    }
}
