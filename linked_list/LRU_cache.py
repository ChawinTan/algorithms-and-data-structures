from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: 'int'):
        self.dicty = collections.OrderedDict()
        self.remain = capacity
        

    def get(self, key: 'int') -> 'int':
        if key not in self.dicty:
            return -1
        v = self.dicty.pop(key)
        self.dicty[key] = v
        return v

    def put(self, key: 'int', value: 'int') -> 'None':
        if key not in self.dicty:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dicty.popitem(last=False)
            self.dicty[key] = value
        else:
            self.dicty.pop(key)
            self.dicty[key] = value
        # print(self.dicty)
