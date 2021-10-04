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





