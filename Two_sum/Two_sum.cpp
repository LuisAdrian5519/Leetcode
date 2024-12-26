//Solution 1 | Brute force

#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {

        int size = nums.size();

        for (int i=0; i<size; i++){
            for(int j = i + 1; j<size; j++){

                if(nums[i] + nums[j] == target){
                    return {i, j};
                }
            }
        }
        return {};
    }
};

int main() {
    // Create a Solution class Object
    Solution solution;

     // Vector & Target Definition
    std::vector<int> nums = {3, 2, 4};
    int target = 6;

     // Twosum function call
    std::vector<int> result = solution.twoSum(nums, target);

    // Result display
    if (!result.empty()) {
        std::cout << "Output: [" << result[0] << ", " << result[1] << "]" << std::endl;
    } else {
        std::cout << "There is no possible combination" << std::endl;
    }

    return 0;
}
