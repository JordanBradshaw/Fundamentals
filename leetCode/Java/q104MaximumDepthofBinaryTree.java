/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Runtime: 1 ms, faster than 20.01% of Java online submissions for Maximum Depth of Binary Tree.
Memory Usage: 40.4 MB, less than 22.00% of Java online submissions for Maximum Depth of Binary Tree.
*/

public class q104MaximumDepthofBinaryTree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

     public static class dfsRunner {
        int totalDepth = 1;

        public dfsRunner() {

        }

        public void inOrder(TreeNode root, int currentDepth) {
            if (root == null)
                return;
            if (root.left != null) {
                inOrder(root.left, currentDepth + 1);
                totalDepth = Math.max(totalDepth, currentDepth + 1);
            }
            if (root.right != null) {
                inOrder(root.right, currentDepth + 1);
                totalDepth = Math.max(totalDepth, currentDepth + 1);
            }
        }

        public int maxDepth(TreeNode root) {
            if (root == null) return 0;
            inOrder(root, 1);
            return totalDepth;
        }

    }

    public static void main(String[] args) {
        dfsRunner runner = new dfsRunner();
        return runner.maxDepth(root);
    }
}
