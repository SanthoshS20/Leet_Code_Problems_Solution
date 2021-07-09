/*

Link - https://leetcode.com/problems/reverse-string/


Problem Description :

Write a function that reverses a string. The input string is given as an array of characters s

*/


/*

Time Complexity   Space Complexity
     O(n)              O(1)

*/


void reverseString(char* s, int sSize){
    int i,j;
    char temp;
    for(i=0, j = sSize-1;i<j;i++,j--)
    {
        temp = *(s+i);
        *(s+i) = *(s+j);
        *(s+j) = temp;
    }
    for(i=0;i<sSize;i++)
    {
        printf("%c", *(s+i));
    }
}



