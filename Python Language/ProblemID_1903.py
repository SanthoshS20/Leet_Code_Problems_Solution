"""

Link - https://leetcode.com/problems/largest-odd-number-in-string/

Problem Description:

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

"""

#     Time Complexity     Space Complexity
#         O(N)                 O(1)



class Solution:
    def largestOddNumber(self, num: str) -> str:
        num_list = list(num)
        length = len(num_list)
        index = length - 1
        flag=0
        while(index>-1):
            if((ord(num_list[index])-48)%2!=0):
                flag=1
                break
            index-=1
        new_string = ""
        if(flag==1):
            for i in range(index+1):
                new_string+=num_list[i]
        return new_string
            
                
        

