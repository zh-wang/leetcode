// ⭐️
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    private ListNode mHead;

    public TreeNode sortedListToBST(ListNode head) {
        int cnt = 0;
        mHead = head;
        ListNode runner = head;
        while (runner != null) {
            runner = runner.next;
            cnt += 1;
        }
        return toBST(0, cnt-1);
    }

    /**
     * `toBST` will be called exactly K times, which K == len of the list.
     * Each time the left search part of `toBST` is finished,
     * move `mHead` forward by 1.
     * This movement means that 'we found a local root'.
     * Then connect left part and right part to that local root.
     */
    public TreeNode toBST(int s, int t) {
        if (s > t) {
            return null;
        }
        int mid = (s + t) / 2;
        TreeNode left = toBST(s, mid - 1);
        TreeNode node = new TreeNode(mHead.val);
        mHead = mHead.next;
        TreeNode right = toBST(mid + 1, t);
        node.left = left;
        node.right = right;
        return node;
    }
}
