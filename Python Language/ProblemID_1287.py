"""

Link - https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Problem Description :

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

"""

#     Time Complexity     Space Complexity
#          O(N)               O(N)

# Either import List like below or use ( list ).
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        values = dict()
        for each_val in arr:
            if each_val not in values:
                values[each_val] = 1
            else:
                values[each_val] += 1
        large = 0
        key_store = 0
        for key,val in values.items():
            if(val>large):
                large = val
                key_store = key
        print(key_store)
        return key_store
        
