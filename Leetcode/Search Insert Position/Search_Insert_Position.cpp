// Solution 1 | Original

#include <iostream>
#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {

        return Binarysearch(nums, target, 0, nums.size()-1);

    }

private: 

    int Binarysearch(std::vector<int>& nums, int target, int low, int high) {

        if (low > high) {
            return low;
        }

        int val = low + (high - low) / 2; // 0.5 jumps

        if (nums[val] == target) {
            return val;
        } else if (nums[val] < target) {
            return Binarysearch(nums, target, val + 1, high);
        } else {
            return Binarysearch(nums, target, low, val - 1);

        }
    }
};