/*
https://leetcode.com/problems/3sum/

Runtime: 296 ms, faster than 67.42% of C# online submissions for 3Sum.
Memory Usage: 36.7 MB, less than 29.04% of C# online submissions for 3Sum.
*/
public class Solution
{
        public IList<IList<int>> ThreeSum(int[] nums)
    {
        IList<IList<int>> retList = new List<IList<int>>();
        if (nums.Length < 3) return retList;
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1, k = nums.Length - 1;
            while (j < k){
                int ThreeSum = nums[i]+ nums[j]+ nums[k];
                if (ThreeSum > 0) k--;
                else if (ThreeSum < 0) j++;
                else{
                    IList<int> aList = new List<int>(){nums[i],nums[j],nums[k]};
                    retList.Add(aList);
                    j++;
                    while(nums[j] == nums[j-1] && j < k) j++;
                }
            }
        }
        return retList;
    }
}
