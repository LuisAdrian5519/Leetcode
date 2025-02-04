//Solution 1 | Original

#include <iostream>
#include <vector>

class Solution {
public:
    bool isPalindrome(int x) {

    if (x < 0) return false;

    int i=0;

    std::string strnum = std::to_string(x);
    int size = strnum.size();

    // Check if characters are equal from both ends
    while (i < size / 2) {
        if (strnum[i] != strnum[size - i - 1]) {
            return false; // Not a palindrome
        }
        i++;
    }

    // If the loop completes, it's a palindrome
    return true;
    }
};
