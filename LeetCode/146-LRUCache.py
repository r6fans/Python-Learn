class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.tail = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        


    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)