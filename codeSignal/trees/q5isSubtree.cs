/*
Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.
*/

//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   public T value { get; set; }
//   public Tree<T> left { get; set; }
//   public Tree<T> right { get; set; }
// }
bool isSubtree(Tree<int> t1, Tree<int> t2)
{
    if (t1 == null && t2 == null)
    {
        return true;
    }
    else if (t1 != null && t2 == null)
    {
        return true;
    }
    else if (t1 == null && t2 != null)
    {
        return false;
    }
    List<int> tree1 = new List<int>();
    List<int> tree2 = new List<int>();
    Stack<Tree<int>> potentialNodes = new Stack<Tree<int>> { };
    void inOrderStack(Tree<int> currentTree)
    {
        if (currentTree.left != null)
        {
            inOrderStack(currentTree.left);
        }
        if ((int)currentTree.value == (int)t2.value)
        {
            potentialNodes.Push(currentTree);
        }
        if (currentTree.right != null)
        {
            inOrderStack(currentTree.right);
        }
    }
    //LOAD KEY NODES
    inOrderStack(t1);

    void inOrderTraversal(Tree<int> currentTree, int currentNum)
    {
        if (currentTree.left != null)
        {
            inOrderTraversal(currentTree.left, currentNum);
        }
        if (currentNum == 1)
        {
            tree1.Add(currentTree.value);
        }
        else
        {
            tree2.Add(currentTree.value);
        }
        if (currentTree.right != null)
        {
            inOrderTraversal(currentTree.right, currentNum);
        }
    }

    //LOAD SUBTREE
    inOrderTraversal(t2, 2);
    foreach (Tree<int> i in potentialNodes)
    {
        inOrderTraversal(i, 1);
        if (tree1.SequenceEqual(tree2) == true)
        {
            return true;
        }
        tree1.Clear();
    }
    return false;
}
