# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        newlist = ListNode('')       
        if val == head.val:
            newlist = self.removeElements(head.next, val)
        else:
            newlist.val = head.val
            newlist.next = self.removeElements(head.next, val)

        return newlist
