// https://leetcode.com/problems/add-two-numbers/

/*
Problem Description 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Time Complexity    Space Complexity
    O(N^2)             O(1)
*/
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, cnt = 0;
        ListNode *head = new ListNode();
        ListNode *runner = head;
        while(l1 || l2){
            int sum = carry;
            if(l1)sum += l1->val, l1 = l1->next;
            if(l2)sum += l2->val, l2 = l2->next;

            carry = sum/10;
            sum %= 10;
            
            if(cnt++ == 0)runner->val=sum;
            else{
                ListNode *curr = new ListNode(sum);
                runner->next = curr;
                runner = curr;
            }
        }
        if(carry){
            ListNode *curr = new ListNode(carry);
            runner->next = curr;
        }
		
        return head;
    }
};