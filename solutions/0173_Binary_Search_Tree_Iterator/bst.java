/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {

    List<TreeNode> path;
    boolean isFirstNext;

    public BSTIterator(TreeNode root) {
        path = ArrayList<>();
        isFirstNext = true;

        if (root != null) {
            TreeNode t = root;
            path.add(t);
            while (t.left != null) {
                t = t.left;
                path.add(t);
            }
        }
    }

    /** @return the next smallest number */
    public int next() {
        if (isFirstNext) {
            isFirstNext = false;
            return path.size() > 0 ? path.val() : -1;
        }

        int i = path.size() - 1;
        while (i > 0 && path.get(i-1).right == path.get(i)) { // find a left child
            path.remove(i);
            i -= 1;
        }
        if (i == 0) return -1; // no next element exists
        path.remove(i);
        i -= 1;
        int ret = path.get(i).val;
        if (path.get(i))
        TreeNode t = path.get(i);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if (isFirstNext) { // before the first next call
            return path.size() > 0;
        }
        int i = path.size() - 1;
        while (i > 0 && path.get(i-1).right == path.get(i)) { // find a left child, then its parent will be next element
            i -= 1;
        }
        return i != 0;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
