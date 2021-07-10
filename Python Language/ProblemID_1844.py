"""
Link - https://leetcode.com/problems/replace-all-digits-with-characters/



Problem Description

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).




Time Complexity      Space Complexity
     O(N)                 O(N)

"""



class Solution:
    def replaceDigits(self, s: str) -> str:
        length = len(s)
        new_string = ""
        for index in range(length):
            if(ord(s[index])>=48 and ord(s[index])<=57):
                new_string += chr(ord(s[index-1])+ord(s[index])-48)
            else:
                new_string += s[index]
        print(new_string)
        return new_string
        
        
        
