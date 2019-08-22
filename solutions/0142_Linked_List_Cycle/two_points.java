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
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        // Suppose there are k steps to entering loop.
        // Thus fast node will have k steps lead from the start of loop, when both nodes enter.
        // Let the steps two nodes meet to be x.
        // When they meets, slow node will be at x-th position.
        // Fast node will be at (k + 2x) - n position. (Fast node goes one loop to catch slow node)
        // x = (k + 2x) - n   ===>   x = n - k
        // Then we can simutaniously move head and slow node by k steps, they will meet at the loop start.
        // =============================
        // This even holds when k > n.
        // let k = p*n + q, this means when slow entering loop, fast node has already run at least p loops
        // We can consider q as the original k, then x = n - q
        // Therefore moving head and slow node by p*n + q steps, they will meet at the loop start
        if (slow.next == null) return null;
        if (fast.next == null || fast.next.next == null) return null;
        slow = slow.next;
        fast = fast.next.next;
        while (slow != fast) {
            if (slow.next == null) return null;
            if (fast.next == null || fast.next.next == null) return null;
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode runner = head;
        while (runner != slow) {
            runner = runner.next;
            slow = slow.next;
        }
        return slow;
    }
}
