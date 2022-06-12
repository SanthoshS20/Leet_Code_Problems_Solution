// https://leetcode.com/problems/reverse-linked-list/

/*

Problem Description 

Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity    Space Complexity
    O(N)             O(1)

*/

#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode
{
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *pushNode(ListNode *head, int data)
{
  ListNode *node = new ListNode(data);
  if (head == NULL)
  {
    head = node;
    return head;
  }

  ListNode *temp = head;

  // Add node to end of Linked List
  while (temp->next != NULL)
    temp = temp->next;
  temp->next = node;
  return head;
}

void printList(ListNode *head)
{
  ListNode *temp = head;
  while (temp != NULL)
  {
    cout << temp->val << " ";
    temp = temp->next;
  }
  cout << "\n";
}

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

int main()
{
  vector<int> v = {1, 2, 3, 4, 5};
  ListNode *head = NULL;

  // Add elements in Linked List
  for (auto &i : v)
    head = pushNode(head, i);

  // Print original Linked List
  printList(head);

  Solution solution;
  head = solution.reverseList(head);

  // Print reversed Linked List
  printList(head);
  return 0;
}