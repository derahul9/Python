class LRUCache:
    def __init__(self, capacity: int):
        #for i range(len(capacity)):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            return self.cache[key]

    def put(self, key: int, value: int):
        if len(self.cache.keys()) == self.capacity:
            self.cache.popitem()                           #As per the question we need to pop the most unused item that is the first key that was inserted.
        self.cache[key] = value                            #This is possible using ordered dictionary. I am popping the most recent entry which might not be correct.
                                                           #Works for 9/18 test cases

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print (lRUCache.get(1))
lRUCache.put(3, 3)
print (lRUCache.get(2))
lRUCache.put(4, 4)