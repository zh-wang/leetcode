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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Deque<TreeNode> s1 = new ArrayDeque<>();
        Deque<TreeNode> s2 = new ArrayDeque<>();
        if (!addBoth(s1, s2, p, q)) {
            return false;
        }
        while (s1.size() > 0 && s2.size() > 0) {
            TreeNode t1 = s1.pop();
            TreeNode t2 = s2.pop();
            if (!addBoth(s1, s2, t1.left, t2.left)) {
                return false;
            }
            if (!addBoth(s1, s2, t1.right, t2.right)) {
                return false;
            }
        }
        return s1.size() == s2.size();
    }

    private boolean addBoth(Deque<TreeNode> s1, Deque<TreeNode> s2,
                        TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return true;
        }
        if (t1 != null && t2 != null && t1.val == t2.val) {
            s1.push(t1);
            s2.push(t2);
            return true;
        }
        return false;
    }
}
