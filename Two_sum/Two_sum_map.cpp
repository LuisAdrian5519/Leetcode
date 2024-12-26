//Solution 3 | Two-Pass Hash table

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
            hashMap[nums[i]] = i; //Save value and nums index
        }

        //Second pass
        for(int i=0; i<nums.size(); i++) {
            int complement = target - nums[i];

            if(hashMap.find(complement) != hashMap.end() && hashMap[complement] != i) {
                return {i, hashMap[complement]};
            }
        }
        return {};
    }
};