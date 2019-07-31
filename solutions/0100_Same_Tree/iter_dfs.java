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
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        Stack<Integer> s3 = new Stack<>();
        if (!addBoth(s1, s2, s3, p, q, 0)) {
            return false;
        }
        while (s1.size() > 0) {
            TreeNode t1 = s1.pop();
            TreeNode t2 = s2.pop();
            int step = s3.pop();
            if (step == 1) {
                if (!addBoth(s1, s2, s3, t1, t2, step + 1)) {
                    return false;
                }
                if (!addBoth(s1, s2, s3, t1.right, t2.right, 0)) {
                    return false;
                }
            } else if (step == 0) {
                if (!addBoth(s1, s2, s3, t1, t2, step + 1)) {
                    return false;
                }
                if (!addBoth(s1, s2, s3, t1.left, t2.left, 0)) {
                    return false;
                }
            }
        }
        return s1.size() == s2.size();
    }

    private boolean addBoth(Stack<TreeNode> s1, Stack<TreeNode> s2, Stack<Integer> s3,
                        TreeNode t1, TreeNode t2, int step) {
        if (t1 == null && t2 == null) {
            return true;
        }
        if (t1 != null && t2 != null && t1.val == t2.val) {
            s1.push(t1);
            s2.push(t2);
            s3.push(step);
            return true;
        }
        return false;
    }
}
