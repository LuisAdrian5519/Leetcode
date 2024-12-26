//Solution 4 | One-Pass Hash table

// For each iteration, we save the complement, add a value of the array to the HashMap, and check if the complement is in the hashMap

#include <iostream>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {

        // Create a Hashmap for values and index
        std::unordered_map<int, int> hashMap;

        //Fist pass
        for(int i=0; i<nums.size(); i++) {
            int complement = target - nums[i];
            if(hashMap.find(complement) != hashMap.end() && hashMap[complement] != i) {
                return {i, hashMap[complement]};
            }
            hashMap[nums[i]] = i; //Save value and nums index

        }
        return {};
    }
};