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

    private List<TreeNode> nodes;

    public void recoverTree(TreeNode root) {
        nodes = new ArrayList<>();
        // map the tree into inorder list
        inorder(root);
        TreeNode e1 = null;
        TreeNode e2 = null;
        Integer lastVal = null;
        TreeNode lastNode = null;
        // find the reversed order in that list
        for (TreeNode node : nodes) {
            if (lastVal == null) {
                lastVal = node.val;
                lastNode = node;
            } else {
                if (e1 == null) { // the first descending element
                    if (lastVal > node.val) {
                        e1 = lastNode;
                        e2 = node; // e2 will be updated each time when desceding element is found
                    }
                } else { // the last descending element
                    if (lastVal > node.val) {
                        e2 = node;
                    }
                }
                lastVal = node.val;
                lastNode = node;
            }
        }
        int temp = e1.val;
        e1.val = e2.val;
        e2.val = temp;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        nodes.add(node);
        inorder(node.right);
    }
}

