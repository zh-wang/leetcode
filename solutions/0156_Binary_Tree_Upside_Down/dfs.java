// --Link--
// https://www.lintcode.com/problem/binary-tree-upside-down/description

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: new root
     */
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        // write your code here
        return flip(root);
    }

    public TreeNode flip(TreeNode node) {
        if (node == null) return null;
        if (node.left == null && node.right == null) return node;
        TreeNode l = flip(node.left);
        TreeNode r = node.right; // maybe null
        // find l's rightmost successor
        TreeNode runner = l;
        while (runner.right != null) runner = runner.right;

        node.left = null;
        node.right = null;
        runner.left = r;
        runner.right = node;
        return l;
    }
}
