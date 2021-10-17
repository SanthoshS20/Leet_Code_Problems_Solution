// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

/*

Problem Description 

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

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
  int maxProfit(vector<int> &prices)
  {
    int res = 0;
    int n = prices.size();
    for (int i = 0; i < n - 1; i++)
    {
      if (prices[i + 1] > prices[i])
        res += prices[i + 1] - prices[i];
    }
    return res;
  }
};

int main()
{
  vector<int> prices = {7, 1, 5, 3, 6, 4};
  Solution solution;
  cout << solution.maxProfit(prices) << '\n';
  return 0;
}