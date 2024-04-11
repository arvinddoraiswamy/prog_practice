# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = head
            even = head.next
            orig_even = even
            while (odd and even and odd.next and even.next):
                odd.next = odd.next.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            
            odd.next = orig_even
        return head
