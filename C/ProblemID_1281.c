/*
Link -   https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Problem Description : 
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
*/

//     Time Complexity     Space Complexity
//        O(log n)              O(1)

#include<stdio.h>
int subtractProductAndSum(int n);
void main()
{
    int num;
    printf("Enter the number:");
    scanf("%d",&num);
    printf("The Difference between product and sum of %d is %d",num,subtractProductAndSum(num));
}
int subtractProductAndSum(int n)
{
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





