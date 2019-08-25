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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if (root == null) return ret;
        Stack<TreeNode> rChilds = new Stack<>();
        Stack<Integer> centers = new Stack<>();
        centers.push(root.val);
        TreeNode cur = root; // always keep left child
        while (cur != null) {
            centers.push(cur.val);
            rChilds.push(cur.right);
            cur = cur.left; // recur on left child
            if (cur == null) { // no left child
                // pop until we found a valid right child as cur
                while (rChilds.size() > 0 && cur == null) {
                    // cur has no child, add its value, then go to parent's right child
                    ret.add(centers.pop());
                    cur = rChilds.pop();
                }
            }
        }
        return ret;
    }
}
