"""

Link - https://leetcode.com/problems/kth-missing-positive-number/

Problem Description :

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

"""

#   Time Complexity   Space Complexity
#    O(max(arr)+k)        O(1)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        large = 0
        length = len(arr)
        for each_element in arr:
            if(each_element>large):
                large = each_element
        large_miss_no = large + k
        count=0
        for index in range(1, large_miss_no+1):
            if index not in arr:
                count+=1
                if(count==k):
                    return index
        
                
        
