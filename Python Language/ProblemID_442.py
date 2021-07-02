# https://leetcode.com/problems/find-all-duplicates-in-an-array/

"""
Problem Description

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
return an array of all the integers that appears twice.

"""

# Time Complexity and Space Complexity
# O(N) and O(N)   

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
    
    

# Time Complexity and Space Complexity
# O(n) and O(1)    
    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicates = list()
        for each_val in nums:
            index = each_val % n
            nums[index] += n
        for i in range(1, n):
            if(nums[i]>(2*n)):
                duplicates.append(i)
        if(nums[0]>(2*n)):
            duplicates.append(n)
        return duplicates
    
    

