// https://leetcode.com/problems/maximum-subarray/

/*

Problem Description 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Time Complexity    Space Complexity
    O(N)             O(1)

*/

#include <iostream>
#include <climits>
#include <vector>

using namespace std;

class Solution
{
public:
  int maxSubArray(vector<int> &nums)
  {
    int cs = 0;
    int ms = INT_MIN;
    for (auto &i : nums)
    {
      cs += i;
      ms = max(ms, cs);
      if (cs < 0)
        cs = 0;
    }
    return ms;
  }
};

int main()
{
  vector<int> v = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
  Solution solution;
  cout << solution.maxSubArray(v) << '\n';
  return 0;
}