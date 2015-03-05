class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.keys = []
        self.dic = {}
        self.cap = capacity

    # @return an integer
    def get(self, key):
        value = -1
        if self.dic.has_key(key):
            value = self.dic[key]
            self.keys.append(self.keys.pop(self.keys.index(key)))
        return value
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.dic.has_key(key):
            self.keys.append(self.keys.pop(self.keys.index(key)))
        else:
            if len(self.keys) >= self.cap:
                self.dic.pop(self.keys.pop(0))
            self.keys.append(key)
        self.dic[key] = value
