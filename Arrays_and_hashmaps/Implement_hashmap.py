'''
Hashmap is a set of key-value pairs
No duplicate keys
O(1) for add, get, delete functions

Components:
1. Array - data structure to store data
2. Hash function - function to convert key into an array index
3. Collision handling - A collision is a situation where hash function maps 2 indexes to the same position in an array
                      - Use a list inside the cell to store the other value

Performance of hashmap depends on distributing the hash value evenly across list cells
'''

class HashMap:
    def __init__(self):
        self.size = 6 #size of the array)
        self.map = [None]*self.size

    def __get_hash(self, key):   #hashing function to get key
        hash_val = 0
        for char in str(key):
            hash_val += ord(char)
        return hash_val % self.size
        
    def add(self, key, value):
        key_hash = self.__get_hash(key)    #get hash value
        key_value = [key, value]           #store key_value

        if self.map[key_hash] is None:     #if position is empty, create a new list in that cell
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:  #check if key exist
                if pair[0] == key:
                    pair[1] = value        #if it exist, override
                    return True
            self.map[key_hash].append(key_value)  #if not, add a new key_value pair
            return True

    def get(self, key):
        key_hash = self.__get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hash_key = self.__get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:   #check the key
                self.map[key_hash].pop(i)    #pop the item at the index
                return True

    def Print(self):
        for item in self.map:
            if item is not None:
                print(str(item))
