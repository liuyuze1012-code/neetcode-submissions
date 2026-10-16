class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        # 1000 empty ListNode in a list
        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key):
        # return the index based on the key value
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        # find the node inside the map that matches the key
        cur = self.map[self.hash(key)]
        # if there is a next val
        while cur.next:
            # 
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                # we remove a value by linking the cur node with the
                # the node after the next node
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)