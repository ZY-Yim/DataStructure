# this file is about hash table

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)
    
    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size 
    
    # the put function assumes that there will eventually be an empty slot 
    # unless the key is already present in the self.slots. 
    def put(self, key, data):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data
    
    def get(self, key):
        start_slot = self.hash_function(key)
        
        data = None
        stop = False
        found = False
        pos = start_slot

        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                stop = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos)
            
            if pos == start_slot:
                stop = True

        return data

h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print(h.slots)
print(h.data)
print(h[55])
print(h[20])
h[20] = 'duck'
print(h[20])