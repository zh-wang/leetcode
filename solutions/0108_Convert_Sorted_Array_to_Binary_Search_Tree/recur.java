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
    public TreeNode sortedArrayToBST(int[] nums) {
        return toBST(nums, 0, nums.length - 1);
    }

    private TreeNode toBST(int[] nums, int s, int t) {
        if (s > t) {
            return null;
        }
        int mid = (s + t) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = toBST(nums, s, mid - 1);
        root.right = toBST(nums, mid + 1, t);
        return root;
    }
}
