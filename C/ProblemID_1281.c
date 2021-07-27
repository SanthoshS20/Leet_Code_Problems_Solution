/*

Link -   https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


Problem Description : 

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

*/

//     Time Complexity     Space Complexity
//        O(log n)              O(1)


int subtractProductAndSum(int n){
    int product = 1;
    int sum = 0;
    while(n!=0)
    {
        int val = n%10;
        product *= val;
        sum += val;
        n = n/10;
    }
    return product - sum;
}





