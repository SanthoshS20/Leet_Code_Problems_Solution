# https://leetcode.com/problems/unique-number-of-occurrences/

"""

Problem Description

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

"""

# Time Complexity  Space Complexity
#     O(n)            O(n)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numbers = dict()
        count_list = []
        for each_val in arr:
            if each_val not in numbers:
                numbers[each_val] = 1
            else:
                numbers[each_val] += 1
        flag=0
        for number, count in numbers.items():
            if count not in count_list:
                count_list.append(count)
            else:
                flag=1
                break
        if(flag==1):
            return False
        else:
            return True
          
          
          
          
          
