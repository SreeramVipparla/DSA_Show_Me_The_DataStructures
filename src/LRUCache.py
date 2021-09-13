from collections import OrderedDict


class Recently_used_cache(object):
    def __init__(self):
        self.data = OrderedDict()

    def empty(self):
        return len(self.data) == 0

    def Delete(self):
        if self.empty():
            return None
        else:
            self.data.popitem(last=False)[0]

    def push(self, integers):
        for integers in self.data:
            self.data.pop(integers)
        self.data[integers] = integers
        return self


class LRU_Cache(object):
    def __init__(self, maximum_capacity):
        self.least_recently_used_cache = Recently_used_cache()
        self.maximum_capacity = maximum_capacity
        self.cache = dict()

    def capacity_limit_confirmation(self):
        if self.maximum_capacity <= len(self.cache):
            return True
        else:
            return False

    def bool_confirmation(self, info):
        if info in self.cache:
            return True
        else:
            return False

    def capacity_limit_confirmation(self):
        if self.maximum_capacity <= len(self.cache):
            return True
        else:
            return False

    def get(self, info):
        if not self.bool_confirmation(info):
            return -1
        else:
            self.least_recently_used_cache .push(info)
            return self.cache[info]

    def set(self, key, value):
        """Add the given key / value pair to the cache"""
        if self.capacity_limit_confirmation():
            lru_key = self.least_recently_used_cache .Delete()
            if lru_key is None:
                pass
            else:
                del self.cache[lru_key]
        self.cache[key] = value
        self.least_recently_used_cache .push(key)


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# Test Cases
# Test case 1
print(our_cache.get(1))
# Expected output
# 1

# Test case 2
print(our_cache.get(2))
# Expected output
# 2

# Test case 3
print(our_cache.get(9))
# Expected output
# -1

# Edge Cases
# Edge case 1
our_cache = LRU_Cache(0)
our_cache.set(1, 2)

print(our_cache.get(10))

# Expected output
# -1
# Edge case 2
our_cache = LRU_Cache(-1)
our_cache.set(1, 2)

print(our_cache.get(10))
# Expected output
# -1
