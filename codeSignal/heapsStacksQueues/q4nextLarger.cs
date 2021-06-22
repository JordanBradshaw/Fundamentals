
/*
Given an array a composed of distinct elements, find the next larger element for each element of the array, i.e. the first element to the right that is greater than this element, in the order in which they appear in the array, and return the results as a new array of the same length. If an element does not have a larger element to its right, put -1 in the appropriate cell of the result array.
*/
int[] nextLarger(int[] a)
{
    Stack<int> returnStack = new Stack<int> { };
    Stack<int> mainStack = new Stack<int> { };
    int stackPopper(Stack<int> passedStack, int index)
    {
        Stack<int> tempStack = new Stack<int>(new Stack<int>(passedStack));
        while (tempStack.Count > 0)
            if (tempStack.Peek() > index) return tempStack.Pop();
            else tempStack.Pop();
        return -1;
    }
    for (int i = a.Length - 1; i >= 0; i--)
    {
        mainStack.Push(a[i]);
        returnStack.Push(stackPopper(mainStack, a[i]));
    }
    return returnStack.ToArray();
}
