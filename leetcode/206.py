# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next #Store next node
            head.next = prev #Set next pointer for node
            prev = head #Prev for next node to be set to current node
            head = tmp #Set next node

        return prev
