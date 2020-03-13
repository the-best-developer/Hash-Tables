import hashlib


# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.curr_capacity = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        
        hashed_key = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16)
        return hashed_key


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''


        
        self.resize()

        index = self._hash_mod(key)
        
        if self.storage[index] == None:

            new_node = LinkedPair(key, value)
            self.storage[index] = new_node
            # print(new_node.value)

            self.curr_capacity = self.curr_capacity + 1
            # print("1")
            return
        
        else:
            node = self.storage[index]

            if node.key == key:
                node.value = value
                return

            else:
                while node.next != None:
                    if node.next.key == key:
                        node.next.value = value
                        return

                    node = node.next
                
                new_node = LinkedPair(key, value)
                node.next = new_node
                
                # print(new_node.value)
                self.curr_capacity = self.curr_capacity + 1
            # print("2")
            return



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node == None:
            print("Key not found")
            return

        elif node.key == key:
            self.storage[index] = None
            return
        
        while node.next != None:
            if node.next.key == key:
                node.next = None
                return
            node = node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        node = self.storage[index]
        # print(self.storage)
        # print(index)
        # print(key)

        if node == None:
            return None

        else:
            if key == node.key:
                # print("5")
                return node.value
            else:
                while node.next != None:
                    if node.next.key == key:
                        # print("4")
                        return node.next.value
                    node = node.next
                    


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        if self.curr_capacity + 1 < self.capacity:
            return

        # print(self.storage)
        new_capacity = self.capacity * 2
        new_storage = [None] * new_capacity

        old_capacity = self.capacity
        old_storage = self.storage

        self.storage = new_storage
        self.capacity = new_capacity
        self.curr_capacity = 0

        for i in range(0, old_capacity):
            node = old_storage[i]

            if node == None:
                continue

            else:
                self.insert(node.key, node.value)
          
            while node.next != None:
                self.insert(node.next.key, node.next.value)
                node = node.next
        # print(self.storage)


            

        # print(self.storage)
        # print(self.capacity)



if __name__ == "__main__":
    ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # ht.insert("key-0", "val-0")
    # ht.insert("key-1", "val-1")
    # ht.insert("key-2", "val-2")
    # ht.insert("key-3", "val-3")
    # ht.insert("key-4", "val-4")
    # ht.insert("key-5", "val-5")
    # ht.insert("key-6", "val-6")
    # ht.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    # ht.insert("key-0", "new-val-0")
    # ht.insert("key-1", "new-val-1")
    # ht.insert("key-2", "new-val-2")
    # ht.insert("key-3", "new-val-3")
    # ht.insert("key-4", "new-val-4")
    # ht.insert("key-5", "new-val-5")
    # ht.insert("key-6", "new-val-6")
    # ht.insert("key-7", "new-val-7")
    # ht.insert("key-8", "new-val-8")
    # ht.insert("key-9", "new-val-9")
    
    # # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))


    # # Test resizing
    # # old_capacity = len(ht.storage)
    # # ht.resize()
    # # new_capacity = len(ht.storage)

    # # # print(f("\nResized from {old_capacity} to {new_capacity}.\n"))

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print(ht.retrieve("key-5"))


    # print(len(ht.storage))

    

    # print("")
