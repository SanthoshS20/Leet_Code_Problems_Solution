/*

Link - https://leetcode.com/problems/missing-number/

Problem Description :

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

*/


/*

Time Complexity   Space Complexity
     O(N)              O(1)

*/


int missingNumber(int* nums, int numsSize){
    int totalSum = 0, i;
    totalSum = numsSize * (numsSize + 1)/2;
    for(i=0;i<numsSize;i++)
    {
        totalSum-=*(nums+i);
    }
    return totalSum;
}
