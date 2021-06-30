# https://leetcode.com/problems/find-all-duplicates-in-an-array/

"""
Problem Description

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
return an array of all the integers that appears twice.

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numbers = dict()
        duplicates = []
        for each_val in nums:
            if each_val not in numbers:
                numbers[each_val] = 1
            else:
                duplicates.append(each_val)
        print(duplicates)
        return duplicates
