#https://leetcode.com/problems/check-if-the-sentence-is-pangram/

"""
Problem Description 

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = dict()
        for each_val in sentence:
            if each_val not in alpha:
                alpha[each_val] = 1
            else:
                alpha[each_val] += 1
        if len(alpha.keys()) == 26:
            return True
        else:
            return False
