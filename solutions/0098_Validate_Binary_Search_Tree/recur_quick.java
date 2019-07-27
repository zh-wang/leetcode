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

    private boolean ret = true;

    public boolean isValidBST(TreeNode root) {
        // There is no bounds at first
        return isBST(root, null, null);
    }

    private boolean isBST(TreeNode node, Integer lower, Integer upper) {
        // an empty tree is BST
        if (node == null) {
            return true;
        }
        if (!ret) {
            return false;
        }
        if (lower != null && node.val <= lower) {
            ret = false;
            return false;
        }
        if (upper != null && node.val >= upper) {
            ret = false;
            return false;
        }
        // update lower bound when recur on right child
        if (!isBST(node.right, node.val, upper)) {
            ret = false;
            return false;
        }
        // update upper bound when recur on left child
        if (!isBST(node.left, lower, node.val)) {
            ret = false;
            return false;
        }
        return true;
    }
}
