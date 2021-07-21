"""

Link - https://leetcode.com/problems/count-the-number-of-consistent-strings/

Problem Description :

You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

"""

#    Time Complexity     Space Complexity
#        O(N)                O(N)


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_string = dict()
        for each_char in allowed:
            if each_char not in allowed_string:
                allowed_string[each_char] = 1
            else:
                allowed_string[each_char] += 1
        count=0
        for each_word in words:
            flag=0
            for each_char in each_word:
                if each_char not in allowed_string:
                    flag=1
                    break
            if(flag==0):
                count+=1
        print(count)
        return count


