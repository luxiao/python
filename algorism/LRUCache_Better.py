class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.keys = []
        self.dic = {}
        self.cap = capacity

    # @return an integer
    def get(self, key):
        value = -1
        if key in self.dic:
            value = self.dic[key]
            self.keys.append(self.keys.pop(self.keys.index(key)))
        return value
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        v = self.get(key)
        if v == -1:
            l = len(self.keys)
            if l >= self.cap:
                del self.dic[self.keys.pop(0)]
            self.keys.append(key)
            self.dic[key] = value
        else:
            self.dic[key] = value
