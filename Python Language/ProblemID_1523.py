"""

Link  -  


Problem Description : 

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

"""

#   Time Complexity   Space Complexity
#       O(1)             O(1)


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        val = high - low
        if(low%2!=0 or high%2!=0):
            val = high - low + 1
        if(val%2!=0):
            return (val//2)+1
        else:
            return (val//2)
        

