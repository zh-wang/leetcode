/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        try {
            ListNode slow = head.next;
            ListNode fast = head.next.next;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next.next;
            }
            return true;
        } catch (Exception e) {
            return false;
        }

    }
}
