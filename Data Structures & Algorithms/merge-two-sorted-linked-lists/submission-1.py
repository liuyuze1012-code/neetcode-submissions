# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base case

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            smaller = list1
            rest_of_1, rest_of_2 = list1.next, list2
        else:
            smaller = list2
            rest_of_1, rest_of_2 = list1, list2.next
        
        merged_list = self.mergeTwoLists(rest_of_1, rest_of_2)

        smaller.next = merged_list

        return smaller






        

