"""

Link - https://leetcode.com/problems/move-zeroes/


Problem Description :

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


"""

#      Time Complexity      Space Complexity
#          O(N)                  O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        length = len(nums)
        while(j<length):
            if(nums[j]!=0):
                nums[i] = nums[j]
                i+=1
            j+=1
        while(i<length):
            nums[i] = 0
            i+=1
            
            
            
