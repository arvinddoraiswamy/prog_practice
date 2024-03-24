"""
Remove duplicates from an unsorted linked list
1 -> 4 -> 3 -> 2 -> 2 -> 4
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

l1 = [1,4,3,2,2,4]
nodes = []
vals = []
dup = []

# Setup values
for i in l1:
    nodes.append(Node(i))

# Setup next pointers for nodes
for count, n in enumerate(nodes):
    if count == len(nodes) - 1:
        break
    else:
        n.next = nodes[count+1]

# Find dups and record
for count, n in enumerate(nodes):
    if n.val not in vals:
        vals.append(n.val)
        continue
    else:
        if count == len(nodes) - 1:
            nodes[count - 1].next = None
        else:
            nodes[count - 1].next = n.next
            n.next = None
        dup.append(count)

for index in dup:
    del(nodes[index-1])

for n in nodes:
    print(n.val, n.next)
