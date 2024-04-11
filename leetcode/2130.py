# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = max_sum = 0
        values = []
        while head:
            values.append(head.val)
            n += 1
            head = head.next
        
        for i in range(0, int(n/2)):
            twin_sum = values[i] + values[n - i - 1]
            if twin_sum > max_sum:
                max_sum = twin_sum
        
        return max_sum
