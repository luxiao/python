class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.keys = []
        self.values = []
        self.cap = capacity

    # @return an integer
    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            value = self.values[index]
            self.keys.insert(0, self.keys.pop(index))
            self.values.insert(0, self.values.pop(index))
        else:
            value = -1
        return value
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.keys:
            ind = self.keys.index(key)
            self.keys.pop(ind)
            self.values.pop(ind)
        else:
            l = len(self.keys)
            if l >= self.cap:
                self.keys.pop()
                self.values.pop()
        self.keys.insert(0, key)
        self.values.insert(0, value)
