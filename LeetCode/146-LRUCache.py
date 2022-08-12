class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: DLinkedNode = None
        self.next: DLinkedNode

class DLinkedlist: 
    def __init__(self ):
        self.head = DLinkedNode(0,0)
        self.tail = DLinkedNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_to_head(self, node: DLinkedNode):
        head_next =self.head.next
        self.head.next = None
        head_next.prev = node
        node.next = head_next
        node.prev = self.head
    
    def remove(self, node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_from_tail(self):
        if self.head.next == self.tail:
            return None
        else:
            node = self.tail.prev
            self.remove(node)
            return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keymap: Dict[int, DLinkedNode] = {}
        self.cache = DLinkedlist()
    
    def add_item(self, key: int, value: int):
        node = DLinkedNode(key=key, value=value)
        self.keymap[key] = node
        self.cache.add_to_head(node)
        
    def remove_item(self, key: int):
        node = self.keymap[key]
        self.cache.remove(node)
        del self.keymap[key]
    
    def remove_least_recently(self):
        node = self.cache.remove_from_tail()
        del self.keymap[node.key]
    
    def set_most_recently(self, key: int):
        node = self.keymap[key]
        self.cache.remove(node)
        self.cache.add_to_head(node)

        
    def get(self, key: int) -> int:
        if key in self.keymap:
            self.set_most_recently(key)
            return self.keymap[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.keymap:
            self.keymap[key].value = value
            self.set_most_recently(key)
        else:
            if len(self.keymap) >= self.capacity:
                self.remove_least_recently()
            self.add_item(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# LRU是一种缓存淘汰算法 意思是最近未使用
# 使用hash 和 双向链表的原因是hash表的查找时间复杂度是O(1), 链表的查询和删除时间复杂度为O(1),但查询不方便