//Solution 2 | Optimal

#include <iostream>
#include <vector>


class Solution {
public:
    bool isPalindrome(int x) {

    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }


    int revertedNumber = 0;
    int originalNumber = x;

    // Algorithm
    while (x < revertedNumber) {
        // Add last digit of x to revertedNumber
        revertedNumber = revertedNumber * 10 + x%10;
        //Eliminate the last digit of x
        x /= 10;
    }

    //Reverted / 10 for odd digit count
    return x == revertedNumber || x == revertedNumber / 10;

    }
};