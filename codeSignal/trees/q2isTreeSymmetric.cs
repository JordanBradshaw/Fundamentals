/*
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.
*/

//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   public T value { get; set; }
//   public Tree<T> left { get; set; }
//   public Tree<T> right { get; set; }
// }
bool isTreeSymmetric(Tree<int> t)
{
    if (t is null)
    {
        return true;
    }
    List<String> leftList = new List<String> { };
    List<String> rightList = new List<String> { };
    void convertLeftToList(Tree<int> t)
    {
        if (!object.ReferenceEquals(t, null))
        {
            leftList.Add(Convert.ToString(t.value));
            if (t.left is Tree<int>)
            {
                convertLeftToList(t.left);
            }
            else
            {
                leftList.Add(null);
            }
            if (t.right is Tree<int>)
            {
                convertLeftToList(t.right);
            }
            else
            {
                leftList.Add(null);
            }
        }
    }
    void convertRightToList(Tree<int> t)
    {
        if (!object.ReferenceEquals(t, null))
        {
            rightList.Add(Convert.ToString(t.value));
            if (t.right is Tree<int>)
            {
                convertRightToList(t.right);
            }
            else
            {
                rightList.Add(null);
            }
            if (t.left is Tree<int>)
            {
                convertRightToList(t.left);
            }
            else
            {
                rightList.Add(null);
            }
        }
    }
    if (!object.ReferenceEquals(t.left, null))
    {
        convertLeftToList(t.left);
    }
    if (!object.ReferenceEquals(t.right, null))
    {
        convertRightToList(t.right);
    }
    foreach (string i in leftList)
    {
        Console.Write(i + " ");
    }
    Console.WriteLine("");
    foreach (string i in rightList)
    {
        Console.Write(i + " ");
    }
    return leftList.SequenceEqual(rightList);
}
