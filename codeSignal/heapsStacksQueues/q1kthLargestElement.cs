/*
Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element. 
*/
int kthLargestElement(int[] nums, int k)
{
    Stack<int> s = new Stack<int> { };
    if (nums == null || k == null)
    {
        return 0;
    }
    nums = nums.OrderByDescending(x => x).ToArray();
    return nums[k - 1];
}
