/*
Had to get help on this one https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/1258712/JS-Python-Java-C%2B%2B-or-Easy-Recursive-Solution-w-Explanation

Note: Your solution should have O(inorder.length) time complexity, since this is what you will be asked to accomplish in an interview.

Let's define inorder and preorder traversals of a binary tree as follows:

    Inorder traversal first visits the left subtree, then the root, then its right subtree;
    Preorder traversal first visits the root, then its left subtree, then its right subtree.

*/
//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   public T value { get; set; }
//   public Tree<T> left { get; set; }
//   public Tree<T> right { get; set; }
// }
Tree<int> restoreBinaryTree(int[] inorder, int[] preorder)
{
    Tree<int> treeBuilder(int[] ino, int[] preo)
    {
        Dictionary<int, int> d = new Dictionary<int, int> { };
        for (int i = 0; i < inorder.Length; i++)
        {
            d.Add(ino[i], i);
        }
        return divideTree(preo, d, 0, 0, ino.Length - 1);
    }
    Tree<int> divideTree(int[] preo, Dictionary<int, int> d, int index, int left, int right)
    {
        int rootVal = preo[index], mid = d[rootVal];
        Tree<int> rootNode = new Tree<int> { };
        rootNode.value = rootVal;
        if (mid > left)
            rootNode.left = divideTree(preo, d, index + 1, left, mid - 1);
        if (mid < right)
            rootNode.right = divideTree(preo, d, index + mid - left + 1, mid + 1, right);
        return rootNode;
    }
    return treeBuilder(inorder, preorder);
}
