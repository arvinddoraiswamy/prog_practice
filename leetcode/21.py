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
        newlist1 = ListNode()
        newlist2 = ListNode()
        if list1.val < list2.val:
            newlist.val = list1.val
            newlist.next = list1.next
            list1 = list1.next
            print(f" List 1 less: {newlist}")
            print(newlist)
        elif list1.val > list2.val:
            newlist.val = list2.val
            newlist.next = list2.next
            list2 = list2.next
            print(f" List 2 less: {newlist}")
            print(newlist)
        elif list1.val == list2.val:
            newlist1.val = list1.val
            newlist1.next = list1.next
            newlist2.val = list2.val
            newlist2.next = list2.next
            list1 = list1.next
            list2 = list2.next
            print(f"Both equal: {newlist1}, {newlist2}")
        print('-' * 10)
        return self.mergeTwoLists(list1, list2)
