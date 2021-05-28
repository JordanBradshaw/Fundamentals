/*
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Runtime: 444 ms, faster than 5.10% of C++ online submissions for Two Sum.
Memory Usage: 10.1 MB, less than 25.53% of C++ online submissions for Two Sum.
*/
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> retVec;
        for (int i=0; i<nums.size(); i++) {
            for (int j=i+1; j<nums.size(); j++) {
                if (nums[i]+nums[j]==target) {
                    retVec.push_back(i);
                    retVec.push_back(j);
                }
            }
        }
        return retVec;
    }
};
