"""

Link - https://leetcode.com/problems/concatenation-of-array/

Problem Description 

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

"""


#   Time Complexity     Space Complexity
#        O(1)                O(1) 


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
      
      
    
