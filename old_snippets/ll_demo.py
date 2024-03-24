# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        ptr = node1
        while ptr.next != None:
            print(ptr.val)
            ptr = ptr.next

        if ptr.next == None:
            print(ptr.val)

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

node1.traverse()