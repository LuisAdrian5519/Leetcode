// Solution 1 | Original

#include <iostream>
#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        
        int size = nums.size();
        int k = 1;
        int i=1;

        while (i<size){

            if(nums[i] == nums[i-1]){
                nums.erase(nums.begin() + i);
                size--;
            } else{
                k++;
                i++;
            }
        }
            return k;
        }
};
