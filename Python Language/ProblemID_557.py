"""

Link -  https://leetcode.com/problems/reverse-words-in-a-string-iii/

Problem Description :

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""

#    Time Complexity    Space Complexity
#         O(n)                O(n)



class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split(" ")
        length = len(string_list)
        new_string = ""
        for index in range(length):
            word_list = list(string_list[index])
            i = 0
            j = len(word_list) - 1
            while(i<j):
                word_list[i], word_list[j] = word_list[j], word_list[i]
                i+=1
                j-=1
            new_word = ""
            for each_char in word_list:
                new_word+=each_char
            string_list[index] = new_word
            if index!=length-1:
                new_string+=string_list[index]+" "
        new_string+=string_list[length-1]
        print(new_string)
        return new_string
            
            
        

