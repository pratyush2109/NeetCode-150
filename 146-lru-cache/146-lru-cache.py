from collections import defaultdict

class LRUCache:
    def __init__(self, capacity: int):
        self.max_size=capacity
        self.l=defaultdict(int)

    def get(self, key: int) -> int:
        if self.l[key]:
            val=self.l[key]
            del self.l[key]
            self.l[key]=val
            return self.l[key]-1
        else:
            del self.l[key]
            return -1

    def put(self, key: int, value: int) -> None:
        if self.l[key]:
            del self.l[key]
            self.l[key]=value+1
        elif self.max_size>=len(self.l):
            self.l[key]=value+1
        else:
            del self.l[next(iter(self.l.keys()))]
            self.l[key]=value+1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)