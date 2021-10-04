"""
Link  -  https://leetcode.com/problems/duplicate-zeros/


PROBLEM DESCRIPTION

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function


"""

#   Time Complexity   Space Complexity
#        O(N)              O(1)

# Either import List like below or use ( list ).
# from typing import List

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i=0
        while(i < (len(arr))):
            if(arr[i]==0):
                arr.pop()
                arr.insert(i+1,0)
                i+=1
            i+=1
