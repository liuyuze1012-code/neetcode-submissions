# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 nodes
        # first starts at head
        # second starts at n positions infront of first
        # while second, then first should be the one we remove
        dummy = ListNode(0, head)
        first = dummy
        second = head

        while n > 0:
            second = second.next
            n -= 1

        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dummy.next
        

        