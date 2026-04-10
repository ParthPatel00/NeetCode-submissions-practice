class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.NUM_BUCKETS = 1000
        self.buckets = [Node(-1) for _ in range(self.NUM_BUCKETS)]
        

    def put(self, key: int, value: int) -> None:
        key_hash = key % self.NUM_BUCKETS
        curr = self.buckets[key_hash]

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if not curr.next:
            # This key does not exist, add it
            curr.next = Node(key, value)
        else:
            # This key does exist already at curr.next
            curr.next.value = value
        
    def get(self, key: int) -> int:
        key_hash = key % self.NUM_BUCKETS
        curr = self.buckets[key_hash].next
        
        while curr and curr.key != key:
            curr = curr.next
        
        if not curr:
            # Key not found
            return -1
        
        return curr.value
        

    def remove(self, key: int) -> None:
        key_hash = key % self.NUM_BUCKETS
        curr = self.buckets[key_hash]

        while curr.next and curr.next.key != key:
            curr = curr.next
        
        if not curr.next:
            return

        # Unlink the node to remove it
        curr.next = curr.next.next
