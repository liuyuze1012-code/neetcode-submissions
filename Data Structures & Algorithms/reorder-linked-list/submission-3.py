# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        #           ^slow

        # split into two halves
        second = slow.next
        slow.next = None
        # first:  1 -> 2 -> 3 -> None
        # second: 4 -> 5 -> 6

        # reverse the second half
        prev = None
        current = second
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second = prev
        # second: 6 -> 5 -> 4

        # weave the two together
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        # 1 -> 6 -> 2 -> 5 -> 3 -> 4