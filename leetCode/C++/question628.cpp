/*
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Runtime: 44 ms, faster than 51.19% of C++ online submissions for Maximum Product of Three Numbers.
Memory Usage: 27.5 MB, less than 92.22% of C++ online submissions for Maximum Product of Three Numbers.
*/
#include <vector>

class Solution {
public:
    int maximumProduct(std::vector<int>& nums) {
        const int end=nums.size();
        std::sort(nums.begin(), nums.end());
        return std::max(nums[0]*nums[1]*nums[end-1], nums[end-1]*nums[end-2]*nums[end-3]);
    }
};
