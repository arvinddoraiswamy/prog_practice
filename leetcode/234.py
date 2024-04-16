# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    values = deque()
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if self.values:
            if head.val != self.values[-1]:
                self.values.append(head.val)
            else:
                self.values.pop()
        else:
            self.values.append(head.val)
        print(self.values)
        if head.next == None:
            if not self.values:
                print(f"empty queue {self.values}")
                return True
            else:
                print(f"queue not empty {self.values}")
                return False
        else:
            print(f"list end not reached {head.next}")
        print('-' * 10)
        print
        self.isPalindrome(head.next)
