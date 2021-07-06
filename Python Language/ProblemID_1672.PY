# https://leetcode.com/problems/richest-customer-wealth/submissions/

"""

Problem Description 

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

"""


# Time Complexity    Space Complexity
#     O(N^2)             O(1)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        large = 0
        for each_account in accounts:
            sum=0
            for each_money in each_account:
                sum+=each_money
            if(sum>large):
                large = sum
        return large
        
