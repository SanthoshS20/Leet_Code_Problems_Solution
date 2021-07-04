# https://leetcode.com/problems/maximum-subarray/submissions/

"""
Problem Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

# Time Complexity   Space Complexity
#      O(N)              O(1)

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = - sys.maxsize - 1
        max_value = 0
        for each_num in nums:
            max_value+=each_num
            if(max_value>maximum):
                maximum = max_value
            if(max_value<0):
                max_value = 0
        return maximum
        
        
