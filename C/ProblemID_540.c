/*

Link  -   https://leetcode.com/problems/single-element-in-a-sorted-array/

Problem Description :

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. 
Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

*/

//    Time Complexity    Space Complexity
//        O(N)                O(1)




int singleNonDuplicate(int* nums, int numsSize){
    int i, element = 0;
    for(i=0;i<numsSize;i++)
    {
        element ^= *(nums+i);
    }
    return element;
}


