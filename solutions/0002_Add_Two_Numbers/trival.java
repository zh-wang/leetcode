/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0); // this is a dummy
        ListNode cur = res;

        int carry = 0;
        while (l1 != null || l2 != null) {
            int v1 = 0;
            int v2 = 0;
            if (l1 != null) v1 = l1.val;
            if (l2 != null) v2 = l2.val;
            int nextVal = v1 + v2 + carry;
            if (nextVal >= 10) {
                nextVal -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            cur.next = new ListNode(nextVal);
            cur = cur.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        if (carry > 0) {
            cur.next = new ListNode(carry);
        }
        return res.next;
    }
}
