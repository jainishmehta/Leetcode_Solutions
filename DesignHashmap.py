class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.slot_size = 1000
        self.table_size =1000
        self.table =[[]for _ in range(self.table_size)]
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        slotkey=key// self.slot_size
        hashkey=key% self.table_size
        if len(self.table[hashkey]) ==0:
            self.table[hashkey]=[-1 for _ in range (self.slot_size)]
        self.table[hashkey][slotkey]=value
        return
        
        


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey=key%self.table_size
        slotkey = key//self.slot_size
        
        if len(self.table[hashkey]):
            return self.table[hashkey][slotkey]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashkey=key%self.table_size
        slotkey=key//self.slot_size
        
        if len(self.table[hashkey]):
            self.table[hashkey][slotkey]=-1
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
