"""

Link - https://leetcode.com/problems/string-matching-in-an-array/


Problem Description :

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

"""


#  Time Complexity    Space Complexity
#       O(N^2)            O(N)



class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        length = len(words)
        match_list = []
        for index_i in range(length):
            for index_j in range(length):
                if words[index_i] in words[index_j] and index_i!=index_j:
                    if words[index_i] not in match_list:
                        match_list.append(words[index_i])
        print(match_list)
        return match_list

