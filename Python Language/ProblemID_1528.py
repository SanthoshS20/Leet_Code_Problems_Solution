# https://leetcode.com/problems/shuffle-string/

"""

Problem Description 

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

"""


# Time Complexity   Space Complexity
#   O(len(s))           O(1)

# Either import List like below or use ( list ).
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dummy_string = list(s)
        s = list(s)
        n = len(indices)
        for index in range(n):
            s[indices[index]] = dummy_string[index]
        val = ""
        for each_char in s:
            val += each_char
        return val
        
