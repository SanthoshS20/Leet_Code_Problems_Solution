#  https://leetcode.com/problems/sign-of-the-product-of-an-array/


"""

Problem Description 

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

"""

# Time Complexity   Space Complexity
#      O(n)               O(1)



class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for each_num in nums:
            prod = prod * each_num
        if prod == 0:
            return 0
        elif prod < 0:
            return -1
        else:
            return 1
        
        
        
