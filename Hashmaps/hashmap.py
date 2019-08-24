class HashMap:
    """
    Hashmap clss initializes the map capacity, a list of lists, maximum load factor and the length number of entries
    """
    def __init__(self, load_factor=1.00):
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        self.size = 8  # capacity
        self.hashmap = [[] for i in range(self.size)] #initializes a list of lists
        self.length = 0  # number of entries in the map

    def __len__(self):
        """
        counts the number of association
        """
        return self.length #return the number of entries in the map
    def buckets(self):
        """
        counts the number of slots that your map has for storing items
        """
        return self.size #returns the number of slots available
    def load(self):
        """
    Return the load factor, the ratio of number of entries to buckets.
        """
        load_fact = float(self.length) / self.size
        return load_fact
    def hash_fun(self, key):
        """hash function"""
        return hash(key) % self.size #calls hash function on supplied key and computes the modulus
    def __contains__(self, key):
        """
        determines whether  an  association  with  the  given key exists.
        Returns a boolean
        """
        hash_key = self.hash_fun(key)
        hash_table = self.hashmap[hash_key]
        for pair in hash_table:  # association in buckets
            if key == pair[0]:  # compares key to the supplied one
                return True
        return False
    def __getitem__(self, key):
        """
        determines  which  value  item  is  associ-ated with a given key
        """
        hash_key = self.hash_fun(key)
        hash_table = self.hashmap[hash_key]#buckets
        for items in hash_table: # key-value pair in hash_table
            if items[0] == key:
                return items[1]
        raise KeyError() #if key not in found raises KeyError
    def __setitem__(self, key, value):
        """
        calls self.insert to add a pair
        """
        return self.insert(key, value)
    def insert(self, key, value):
        """
        adds  associations  to the map, checks if the key is not in the map already, then assigns value to the key
        """
        hash_key = self.hash_fun(key)
        hash_table = self.hashmap[hash_key]
        for items in hash_table:  # key-value pair in hash_table
            if items[0] == key:  #if key equal to the given key
                items[1] = value #assigns key the value
                return
        hash_table.append([key, value]) #chaining
        self.length += 1
        if self.load() > self.max_load_factor: #checks map capacity
            self.resize(2) #calls resize to double the size
    def __delitem__(self, key):
        """
        removes  key-value association
        """
        hash_key = self.hash_fun(key)
        hash_table = self.hashmap[hash_key]
        for items in hash_table: # key-value pair in hash_table
            if items[0] == key: #if key equal to the given key
                hash_table.remove([items][0]) #remove that key
                self.length -= 1 #adjust the length
                if self.load() < 0.25:#shrinks the map load factor to 1/4 of the max factor
                    self.resize(0.5) #calls resize and re-adjusts the map size by half
                return
        raise KeyError() #if key not in the map, raises key KeyError
    def __iter__(self):
        """
        iterates through the hashmap and yields the key-value pair
        """
        for pair in self.hashmap: #buckets
            for items in pair: #pair in buckets
                if items is not None: #if pair exists
                    yield items  # Yield key-value pairs
    def clear(self):
        """
        deletes all the associations
        """
        self.size = 16  # capacity
        self.hashmap = [[] for i in range(self.size)] #empty the map
        self.length = 0  # number of entries in the map
    def keys(self):
        """
        function iterates through all the keys
        """
        keys_list = set() #creates a set of keys
        for items in self.hashmap: #checks for buckets in hashmap
            if items is not None:
                for pair in items: #checks for pairs in buckets
                    keys_list.add(pair[0]) #adds key to the set the keys set
        return keys_list
  
    def __repr__(self):
        """
        A string representation of this map
        :return: A string representing this map
        """
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))
    def __bool__(self):
        """
        Checks if there are items in the map
        :return True if the map is non-empty
        """
        return not self.is_empty()
    def is_empty(self):
        """
        Checks that there are no items in the map
        :return: True if there are no bindings
        """
        return len(self) == 0
    # _____________________________________________________________________________________________
    
    def resize(self, factor):
        """
        function to double up or shrink the hashmap
        """
        new_size = self.size * factor#initialize new_size
        old = self.hashmap #copy old hashmap to a temporary map
        self.size = int(new_size) #old size becomes the new size
        self.hashmap = [[] for i in range(int(new_size))] #initialize a new map with the size of new size
        for items in old: #iterates through old map
            for pair in items: #pair in buckets
                new_indx = self.hash_fun(pair[0]) #new index to adjust buckets
  
              self.hashmap[new_indx].append([pair[0], pair[1]]) #append key-value pair to the new hashmap

def year_count(input_hashmap):
    """
    Function to count the number of students born in the given year
    :input: A HashMap of student name and its birth year
    :returns: A HashMap of the year and the number of students born in that year
    """
    hashmap = HashMap()
    for _, year in input_hashmap:
        if year in hashmap:
            hashmap[year] += 1
        else:
            hashmap[year] = 1
    return hashmap
    
