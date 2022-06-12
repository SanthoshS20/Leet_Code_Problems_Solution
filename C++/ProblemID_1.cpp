// https://leetcode.com/problems/two-sum/

/*
Problem Description 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Time Complexity    Space Complexity
    O(N^2)             O(1)
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
	// Declare hashmap (unordered_map)
	std::unordered_map<int, int> map;
	//Declare loop variables
	int i, s = nums.size();
	//Loop over input nums
	map[nums[0]] = 0; // (Optimization) unroll one iteration.
	for(i = 1; i < s; ++i) // (Optimization) Start at 1 instead of 0
	{
		if (map.find(target - nums[i]) != map.end()) return {map[target - nums[i]], i};
		else map[nums[i]] = i;
	}
	return {};
        
    }
};