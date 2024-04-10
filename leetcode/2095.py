# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        orig_head = head
        count = 0
        while head:
            count += 1
            head = head.next
        middle = int(count/2)

        count = 0
        head = orig_head
        while head:
            if middle == 0:
                new_node = ListNode()
                new_node.val = ''
                return new_node
            if count == middle - 1:
                next_node = head.next
                head.next = next_node.next
                next_node.next = None
                break
            else:
                count += 1
                head = head.next
        
        head = orig_head
        return head
