# class DLinkedNode:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev: DLinkedNode = None
#         self.next: DLinkedNode = None

# class DLinkedlist: 
#     def __init__(self ):
#         self.head = DLinkedNode(0,0)
#         self.tail = DLinkedNode(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.size = 0
        
#     def add_to_tail(self, node: DLinkedNode):
#         node.prev = self.tail.prev
#         node.next = self.tail
#         self.tail.prev.next = node
#         self.tail.prev = node
#         self.size+=1
        
    
#     def remove(self, node: DLinkedNode):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         self.size-=1
    
#     def remove_first_node(self):
#         if self.head.next == self.tail:
#             return None
#         first = self.head.next
#         self.remove(first)
#         return first

#     def get_size(self) -> int:
#         return self.size
        

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.hashmap: Dict[int, DLinkedNode] = {}
#         self.cache = DLinkedlist()
    
#     def make_recent(self, key):
#         new_node = self.hashmap.get(key)
#         self.cache.remove(new_node)
#         self.cache.add_to_tail(new_node)
        
#     def add_recent(self, key, val):
#         recent = DLinkedNode(key, val)
#         self.cache.add_to_tail(recent)
#         self.hashmap[key] = recent
    
#     def remove_key(self, key):
#         remove_node = self.hashmap.get(key)
#         self.cache.remove(remove_node)
#         del self.hashmap[key]
    
#     def remove_least_recent(self):
#         least_recent = self.cache.remove_first_node()
#         delete_key = least_recent.key
#         del self.hashmap[delete_key]
        
#     def get(self, key) -> int:
#         if key not in self.hashmap.keys():
#             return -1
#         self.make_recent(key)
#         return self.hashmap.get(key)

#     def put(self, key, val):
#         if key in self.hashmap.keys():
#             self.remove_key(key)
#             self.add_recent(key, val)
#             return
        
#         if self.cache.get_size() == self.capacity:
#             self.remove_least_recent()
        
#         self.add_recent(key, val)
            

class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoubleList:
    def __init__(self):
        # self.head和self.tail都充当dummy节点（哨兵节点）
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, x):
        """在最前面加个节点x，注意语句顺序，很经典！"""
        x.next = self.head.next
        x.prev = self.head
        self.head.next.prev = x
        self.head.next = x
        self.size += 1

    def remove(self, x):
        """删除节点x，调用这个函数说明x一定存在"""
        x.prev.next = x.next  # 像一个顺时针
        x.next.prev = x.prev
        self.size -= 1

    def removeLast(self):
        """
        删除链表中最后一个节点，并返回该节点
        注意双向链表的删除时间复杂度是O(1)的，因为立刻能找到该删除节点的前驱
        """
        if self.size == 0:
            return None
        last_node = self.tail.prev
        self.remove(last_node)
        return last_node

    def getSize(self):
        return self.size



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        new_item = Node(key, value)
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addFirst(new_item)
            self.map[key] = new_item
        else:
            if self.capacity == self.cache.getSize():
                last_node = self.cache.removeLast()
                self.map.pop(last_node.key)
            self.cache.addFirst(new_item)
            self.map[key] = new_item
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# LRU是一种缓存淘汰算法 意思是最近未使用
# 使用hash 和 双向链表的原因是hash表的查找时间复杂度是O(1), 链表的查询和删除时间复杂度为O(1),但查询不方便