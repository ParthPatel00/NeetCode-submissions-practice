class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyHashSet:

    def __init__(self):
        
        self.buckets = [Node(None) for i in range(10000)]

    def add(self, key: int) -> None:
        key_hash = key % 10000

        if self.contains(key):
            return
        self.buckets[key_hash].next = Node(key)
        

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        key_hash = key % 10000

        self.buckets[key_hash].next = None
        

    def contains(self, key: int) -> bool:
        key_hash = key % 10000
        return self.buckets[key_hash].next is not None

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)