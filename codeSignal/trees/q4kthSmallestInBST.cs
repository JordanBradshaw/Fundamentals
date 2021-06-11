/*
Note: Your solution should have only one BST traversal and O(1) extra space complexity, since this is what you will be asked to accomplish in an interview.

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and the right subtrees must also be binary search trees.

Given a binary search tree t, find the kth smallest element in it.
*/
//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   public T value { get; set; }
//   public Tree<T> left { get; set; }
//   public Tree<T> right { get; set; }
// }
int kthSmallestInBST(Tree<int> t, int k)
{
    if (k <= 0)
    {
        return t.value;
    }
    ArrayList alist = new ArrayList { };
    void inOrderTraversal(Tree<int> passedT)
    {
        if (passedT.left != null)
        {
            inOrderTraversal(passedT.left);
        }
        alist.Add(passedT.value);
        if (passedT.right != null)
        {
            inOrderTraversal(passedT.right);
        }
    }

    inOrderTraversal(t);
    return (int)alist[k - 1];
}
