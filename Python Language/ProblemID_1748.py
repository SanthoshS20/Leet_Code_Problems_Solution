# https://leetcode.com/problems/sum-of-unique-elements/submissions/

"""
Problem Description 

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numbers = dict()
        sum = 0
        for each_num in nums:
            sum+=each_num
        for each_num in nums:
            if each_num not in numbers:
                numbers[each_num] = 1
            else:
                if numbers[each_num] == 1:
                    sum = sum - (nums.count(each_num)*each_num)
                    numbers[each_num] = 0
        return sum
                
        
