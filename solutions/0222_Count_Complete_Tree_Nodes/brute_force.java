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
    public int countNodes(TreeNode root) {
        return recur(root);
    }

    private int recur(TreeNode node) {
        if (node == null) return 0;
        return recur(node.left) + recur(node.right) + 1;
    }
}
