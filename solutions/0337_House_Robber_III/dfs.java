/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rob(TreeNode root) {
        Pair<Integer, Integer> ret = dfs(root);
        return Math.max(ret.getKey(), ret.getValue());
    }

    // pick, not pick
    private Pair<Integer, Integer> dfs(TreeNode node) {
        if (node == null) return new Pair<>(0, 0);
        Pair<Integer, Integer> p1 = dfs(node.left);
        Pair<Integer, Integer> p2 = dfs(node.right);
        return new Pair<>(p1.getValue() + p2.getValue() + node.val,
                          Math.max(p1.getKey(), p1.getValue()) +
                          Math.max(p2.getKey(), p2.getValue()));
    }
}
