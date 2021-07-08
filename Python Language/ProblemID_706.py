#  https://leetcode.com/problems/design-hashmap/

"""

Problem Description

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

"""

#   Time Complexity   Space Complexity
#        O(1)               o(1)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.values[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.values:
            return -1
        else:
            return self.values[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.values:
            del self.values[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
