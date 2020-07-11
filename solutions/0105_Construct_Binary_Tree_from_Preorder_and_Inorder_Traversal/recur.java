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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return build(preorder, 0, preorder.length - 1,
                     inorder, 0, inorder.length - 1);
    }

    // preoder looks like root...left_childs...right_childs
    // inorder looks like ...left_childs...root...right_childs
    private TreeNode build(int[] preorder, int a, int b,
                           int[] inorder, int c, int d) {
        if (preorder == null || preorder.length == 0 || a > b || c > d) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[a]);
        if (a == b || c == d) return root;
        int rootIndex = indexOf(inorder, preorder[a], c, d);
        int lenOfLeft = rootIndex - c;
        // then split preorder into two parts
        // left part
        root.left = build(preorder, a + 1, a + 1 + lenOfLeft - 1,
                          inorder,  c,     rootIndex - 1);
        root.right = build(preorder, a + 1 + lenOfLeft, b,
                           inorder,  rootIndex + 1,     d);
        return root;
    }

    private int indexOf(int[] arr, int value, int a, int b) {
        for (int i = a; i <= b; ++i) {
            if (arr[i] == value) return i;
        }
        return -1;
    }
}
