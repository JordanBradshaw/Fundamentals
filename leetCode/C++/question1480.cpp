/*
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Runtime: 4 ms, faster than 57.93% of C++ online submissions for Running Sum of 1d Array.
Memory Usage: 8.4 MB, less than 93.35% of C++ online submissions for Running Sum of 1d Array.
*/
#include <vector>

class Solution {
public:
    std::vector<int> runningSum(std::vector<int>& nums) {
        std::vector<int> retVec;
        retVec.push_back(nums[0]);
        if (nums.size()==1) {
            return retVec;
        }

        for (int i=1; i<nums.size(); i++) {
            ///DOWN RUNNER
            int sumAccum=0;
            for (int j=i; j>=0; j--) {
                sumAccum+=nums[j];
            }
            retVec.push_back(sumAccum);
        }
        return retVec;
    }
};
