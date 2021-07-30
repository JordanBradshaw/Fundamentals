/*
https://leetcode.com/problems/binary-tree-inorder-traversal/

Runtime: 236 ms, faster than 74.50% of C# online submissions for Binary Tree Inorder Traversal.
Memory Usage: 30.5 MB, less than 78.71% of C# online submissions for Binary Tree Inorder Traversal.
*/

public class Solution
{
    public void InorderRecur(TreeNode root, IList<int> intList)
    {
        if (root.left != null) InorderRecur(root.left, intList);
        intList.Add(root.val);
        if (root.right != null) InorderRecur(root.right, intList);
    }

    public IList<int> InorderTraversal(TreeNode root)
    {
        IList<int> retList = new List<int>();
        if (root == null) return retList;
        InorderRecur(root, retList);
        return retList;

    }
}
