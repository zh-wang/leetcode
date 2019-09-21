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

    Stack<TreeNode> nodes; // keep left nodes

    public BSTIterator(TreeNode root) {
        nodes = new Stack<>();
        pushLeftNodes(root);
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode node = nodes.pop(); // the next node
        if (node.right != null) { // push all left children of 'the next node' to stack
            pushLeftNodes(node.right);
        }
        return node.val;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
         return nodes.size() > 0;
    }

    private void pushLeftNodes(TreeNode node) {
        while (node != null) {
            nodes.push(node);
            node = node.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
