/*
1570. Dot Product of Two Sparse Vectors
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

    SparseVector(nums) Initializes the object with the vector nums
    dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Runtime: 352 ms, faster than 95.92% of C# online submissions for Dot Product of Two Sparse Vectors.
Memory Usage: 45.9 MB, less than 34.69% of C# online submissions for Dot Product of Two Sparse Vectors.
*/

public class SparseVector
{
    int[] arr;
    public SparseVector(int[] nums)
    {
        arr = nums;
    }

    public int[] getArr()
    {
        return arr;
    }
    // Return the dotProduct of two sparse vectors
    public int DotProduct(SparseVector vec)
    {
        int[] arr2 = vec.getArr();
        int accumulator = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            accumulator += (arr[i] * arr2[i]);
        }

        return accumulator;
    }
}

// Your SparseVector object will be instantiated and called as such:
//SparseVector v1 = new SparseVector(nums1);
//SparseVector v2 = new SparseVector(nums2);
//int ans = v1.DotProduct(v2);
