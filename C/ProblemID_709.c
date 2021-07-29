/*

Link  - https://leetcode.com/problems/to-lower-case/


Problem Description :

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

*/


//    Time Complexity    Space Complexity
//        O(N)                O(1)





char * toLowerCase(char * s){
    int i;
    for(i=0;*(s+i)!='\0';i++)
    {
        if((*(s+i))>=65 && (*(s+i))<=90)
            *(s+i) = *(s+i) - 65 + 97;
    }
    return s;
}



