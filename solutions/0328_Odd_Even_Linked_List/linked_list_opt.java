/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return null;
        ListNode odd = head, oddHead = new ListNode(0), oddRunner = oddHead;
        ListNode even = head.next, evenHead = new ListNode(0), evenRunner = evenHead;
        while (odd != null && even != null) {
            oddRunner.next = odd;
            oddRunner = oddRunner.next;
            evenRunner.next = even;
            evenRunner = evenRunner.next;
            // find next odd & even
            odd = even.next;
            even = odd == null ? null : odd.next;
            // remove odd & even's next pointer
            oddRunner.next = evenRunner.next = null;
        }
        if (odd != null) {
            oddRunner.next = odd;
            oddRunner = oddRunner.next;
        }
        ListNode root = new ListNode(0);
        root.next = oddHead.next;
        oddRunner.next = evenHead.next;
        return root.next;
    }
}
