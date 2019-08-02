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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        PriorityQueue<Box> q = new PriorityQueue<>((a, b) -> {
            return a.depth - b.depth;
        });
        q.add(new Box(root, 1));
        while (!q.isEmpty()) {
            Box box = q.poll();
            TreeNode node = box.node;
            int depth = box.depth;
            if (node.left == null && node.right == null) {
                return depth;
            } else if (node.left == null) {
                q.add(new Box(node.right, depth + 1));
            } else if (node.right == null) {
                q.add(new Box(node.left, depth + 1));
            } else {
                q.add(new Box(node.right, depth + 1));
                q.add(new Box(node.left, depth + 1));
            }
        }
        return -1;
    }

    private static class Box {
        TreeNode node;
        int depth;
        Box(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}
