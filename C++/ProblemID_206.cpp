// https://leetcode.com/problems/reverse-linked-list/

/*

Problem Description 

Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity    Space Complexity
    O(N)             O(1)

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
  ListNode *Head = NULL;
  void rev(ListNode *head)
  {
    if (head->next == NULL)
    {
      Head = head;
      return;
    }
    rev(head->next);
    ListNode *temp = head->next;
    temp->next = head;
    head->next = NULL;
  }

  ListNode *reverseList(ListNode *head)
  {
    if ((head == NULL) or (head->next == NULL))
      return head;
    rev(head);
    return Head;
  }
};