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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if (root == null) return ret;
        Stack<TreeNode> nodes = new Stack<>();
        nodes.push(root);
        while (nodes.size() > 0) {
            TreeNode cur = nodes.pop();
            ret.add(cur.val);
            if (cur.right != null) nodes.push(cur.right);
            if (cur.left != null) nodes.push(cur.left);
        }
        return ret;
    }
}
