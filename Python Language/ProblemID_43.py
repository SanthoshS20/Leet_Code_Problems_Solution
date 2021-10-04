#https://leetcode.com/problems/multiply-strings/

"""
Problem Description 

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

# Time Complexity    Space Complexity
#     O(m*n)             O(m+n)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        
        num1 = list(map(int,reversed(num1)))
        num2 = list(map(int,reversed(num2)))
        
        res  = [0] * (len1 + len2)
        
        for j in range(len2):
            for i in range(len1):
                res[i+j] += num1[i] * num2[j]
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10
                
        i = len(res) - 1
        while res[i] == 0 and  i > 0:
            i = i-1
            
        return "".join(map(str,res[:i+1][::-1]))


