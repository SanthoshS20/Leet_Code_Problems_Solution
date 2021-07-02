# https://leetcode.com/problems/third-maximum-number/submissions/

"""
Problem Description

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

"""

# Time Complexity   Space Complexity
#   O(N)           O(1)


import sys
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = - sys.maxsize - 1
        second = - sys.maxsize - 1
        third = - sys.maxsize - 1
        if(len(set(nums))>2):
            for each_val in nums:
                if each_val>first:
                    third = second
                    second = first
                    first = each_val
                elif each_val>second and each_val!=first:
                    third = second
                    second = each_val
                elif each_val>third and each_val!=second and each_val!=first:
                    third = each_val
            return third
        else:
            return max(nums)