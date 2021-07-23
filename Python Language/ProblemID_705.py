"""

Link - https://leetcode.com/problems/design-hashset/

Problem Description : 

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

"""

#     Time Complexity   Space Complexity
#         O(1)              O(1)



class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.arr:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

