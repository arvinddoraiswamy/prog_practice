# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return ListNode('')
        if list1 and not list2:
            return list1
        if not list1 and list2:
            return list2

        newlist = ListNode()
        if list1.val <= list2.val:
            newlist.val = list1.val
            newlist.next = self.mergeTwoLists(list1.next, list2)
        else:
            newlist.val = list2.val
            newlist.next = self.mergeTwoLists(list1, list2.next)
        
        return newlist
