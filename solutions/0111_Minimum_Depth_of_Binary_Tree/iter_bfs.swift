/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func minDepth(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }
        var depth: Int = 1
        var la = ArrayWrapper(arr: [root])
        var lb = ArrayWrapper(arr: [])
        while (la.arr.count > 0 || lb.arr.count > 0) {
            var src = la.arr.count > 0 ? la : lb
            var tar = la.arr.count > 0 ? lb : la
            for node in src.arr {
                if (node.left == nil && node.right == nil) {
                    return depth
                } else if (node.left == nil) {
                    tar.arr.append(node.right!)
                } else if (node.right == nil) {
                    tar.arr.append(node.left!)
                } else {
                    tar.arr.append(node.left!)
                    tar.arr.append(node.right!)
                }
            }
            src.arr.removeAll()
            depth += 1
        }
        return depth
    }

    class ArrayWrapper {
        var arr: [TreeNode]

        init(arr: [TreeNode]) {
            self.arr = arr
        }
    }
}
