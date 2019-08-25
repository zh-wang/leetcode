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
        Stack<TreeNode> rChilds = new Stack<>();
        TreeNode cur = root; // always keep left child
        while (cur != null) {
            ret.add(cur.val);
            if (cur.right != null) {
                rChilds.push(cur.right);
            }
            cur = cur.left; // recur on left child
            if (cur == null && rChilds.size() > 0) {
                cur = rChilds.pop();
            }
        }
        return ret;
    }
}
