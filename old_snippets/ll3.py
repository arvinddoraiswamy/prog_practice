# Node Class already in problem - NOT MY CODE
from copy import deepcopy

class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node

    # Only this is my code
    def reverseList(self):
        if self.head is None:
            return None
        else:
            tmp_outer = self.head
            end = n

            for i in range(0, int(n/2)):
                #print(tmp_outer.data)
                tmp = tmp_outer.next
                k = i + 1
                while k < end:
                    if k == end - 1:
                        #print("k", k)
                        #print("current", tmp_outer.data, tmp.data)
                        x1 = tmp.data
                        tmp.data = tmp_outer.data
                        tmp_outer.data = x1
                        #print("swap", tmp_outer.data, tmp.data)
                    k += 1
                    tmp = tmp.next
                tmp_outer = tmp_outer.next
                end = end - 1
                #print('-' * 10)

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reverse_List = reverseList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()
# Contributed by: Harshit Sidhwa
# # Node Class already in problem - NOT MY CODE

"""
d1 = self.head
end = n
for j in range(0, (int(n/2))):
    d2 = deepcopy(d1)
    data1 = d1.data
    k = j + 1
    print("j", j)
    while k < end:
        d1 = d1.next
        k += 1
        if k == end:
            print("before", self.head.data, d1.data)
            self.head.data = d1.data
            d1.data = data1
            print("after swap", self.head.data, d1.data)
    end = n - 1
    d1 = d2.next
    print('-' * 10)
"""