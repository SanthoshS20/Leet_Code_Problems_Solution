"""

Link  -   https://leetcode.com/problems/valid-parentheses/


Problem Description :

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

#    Time Complexity    Space Complexity
#        O(N)               O(N)



class Solution:
    def isValid(self, s: str) -> bool:
        flag=0
        values = []
        for each_char in s:
            if each_char == '(' or each_char == '{' or each_char == '[':
                values.append(each_char)
            else:
                if len(values)==0:
                    flag=1
                    break
                if each_char == ')':
                    pop_ele = values.pop()
                    if pop_ele!= '(':
                        flag=1
                        break
                elif each_char == '}':
                    pop_ele = values.pop()
                    if pop_ele!= '{':
                        flag=1
                        break
                elif each_char == ']':
                    pop_ele = values.pop()
                    if pop_ele!= '[':
                        flag=1
                        break
        if(flag==1):
            return False
        else:
            if(len(values)!=0):
                return False
            else:
                return True
        



