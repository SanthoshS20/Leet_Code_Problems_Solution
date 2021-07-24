"""

Link -  https://leetcode.com/problems/valid-anagram/

Problem Description : 

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""

#   Time Complexity    Space Complexity
#        O(N)              O(N)



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values = dict()
        s_len = len(s)
        t_len = len(t)
        flag=0
        if(s_len == t_len):
            for index in range(s_len):
                if s[index] not in values:
                    values[s[index]] = 1
                else:
                    values[s[index]] += 1
                if t[index] not in values:
                    values[t[index]] = -1
                else:
                    values[t[index]] -=1
            for key,value in values.items():
                if value !=0:
                    flag=1
                    break
            if(flag==1):
                return False
            else:
                return True
        else:
            return False
                    
        


