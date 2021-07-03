# https://leetcode.com/problems/second-largest-digit-in-a-string/

"""

Problem Description

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

"""

# Time Complexity     Space Complexity
#      O(N)                O(N)

class Solution:
    def secondHighest(self, s: str) -> int:
        s_list = list(s)
        integer_list = []
        first = -1
        second = -1
        for each_val in s_list:
            if(ord(each_val) in range(48,58)):
                integer_list.append(int(each_val))
        for each_num in integer_list:
            if(each_num>first):
                second = first
                first = each_num
            elif each_num>second and each_num!=first:
                second = each_num
        return second
        
