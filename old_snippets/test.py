l1=[1,2,3]
l2=l1[:]

print(l2)
for x in l1:
    l2.remove(x)
print(l2)
