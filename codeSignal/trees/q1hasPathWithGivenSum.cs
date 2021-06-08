/*
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.
Binary trees are already defined with this interface:
class Tree<T> {
    public T value { get; set; }
    public Tree<T> left { get; set; }
    public Tree<T> right { get; set; }
 } */
bool hasPathWithGivenSum(Tree<int> t, int s)
{
    if (t == null)
    {
        return false;
    }
    bool trueFlag = false;
    void inOrder(Tree<int> t, List<int> prevList)
    {
        List<int> currList = new List<int>(prevList);
        currList.Add(t.value);
        if (object.ReferenceEquals(t.left, null) && object.ReferenceEquals(t.right, null))
        {
            if (currList.Sum(x => Convert.ToInt32(x)) == s)
            {
                trueFlag = true;
            }
        }
        if (!object.ReferenceEquals(t, null))
        {
            if (t.left is Tree<int>)
            {
                inOrder(t.left, currList);
            }
            Console.WriteLine(t.value);
            if (t.right is Tree<int>)
            {
                inOrder(t.right, currList);
            }
        }
    }
    inOrder(t, new List<int> { });
    if (trueFlag == false)
    {
        return false;
    }
    else
    {
        return true;
    }
}
