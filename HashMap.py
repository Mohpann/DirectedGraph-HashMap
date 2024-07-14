my_list = [None] * 5
my_list.append(5)
print(my_list, len(my_list))
my_list.insert(1, 5)
print(my_list, len(my_list))

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    def getHash(self, key):
        for char in key:
            hash+= ord(char) ## ord() returns integer Unicode char
        return hash % self.size # return index location in array 


"""
Hashmap Python

Set of key/value pairs
No duplicate keys
0(1) for add, get, delete

- AKA map/dictionary/hash table/associative array
- Use dict() 

Components of Hashmap:

Array - data structure used to store data

Hash function - function to convert key into an array index

Collision handling

"""

