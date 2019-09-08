/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> set = new HashSet<>();
        ListNode ra = headA, rb = headB;
        while (ra != null) {
            set.add(ra);
            ra = ra.next;
        }
        while (rb != null) {
            if (set.contains(rb)) return rb;
            rb = rb.next;
        }
        return null;
    }
}
