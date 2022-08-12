class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: DLinkedNode = None
        self.next: DLinkedNode = None

class DLinkedlist: 
    def __init__(self ):
        self.head = DLinkedNode(0,0)
        self.tail = DLinkedNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def add_to_tail(self, node: DLinkedNode):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size+=1
        
    
    def remove(self, node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1
    
    def remove_first_node(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def get_size(self) -> int:
        return self.size
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: Dict[int, DLinkedNode] = {}
        self.cache = DLinkedlist()
    
    def make_recent(self, key):
        new_node = self.hashmap.get(key)
        self.cache.remove(new_node)
        self.cache.add_to_tail(new_node)
        
    def add_recent(self, key, val):
        recent = DLinkedNode(key, val)
        self.cache.add_to_tail(recent)
        self.hashmap[key] = recent
    
    def remove_key(self, key):
        remove_node = self.hashmap.get(key)
        self.cache.remove(remove_node)
        del self.hashmap[key]
    
    def remove_least_recent(self):
        least_recent = self.cache.remove_first_node()
        delete_key = least_recent.key
        del self.hashmap[delete_key]
        
    def get(self, key) -> int:
        if key not in self.hashmap.keys():
            return -1
        self.make_recent(key)
        return self.hashmap.get(key)

    def put(self, key, val):
        if key in self.hashmap.keys():
            self.remove_key(key)
            self.add_recent(key, val)
            return
        
        if self.cache.get_size() == self.capacity:
            self.remove_least_recent()
        
        self.add_recent(key, val)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# LRU是一种缓存淘汰算法 意思是最近未使用
# 使用hash 和 双向链表的原因是hash表的查找时间复杂度是O(1), 链表的查询和删除时间复杂度为O(1),但查询不方便