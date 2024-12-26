//Solution 2 | Brute force++

#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {

        int size = nums.size();
        int x = 0;

        for (int i=0; i<size; i++){
            for (int j=i+1; j<size; j++){

                x = target - nums[i];
                if(nums[j] == x){
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
    std::vector<int> nums = {2,5,5,11};
    int target = 10;

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
