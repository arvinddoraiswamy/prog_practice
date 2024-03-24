import numpy

a = "1 2 3 4 5 6 7 8 9 10 11 12"
values = a.split(' ')
values = [values[i:i+3] for i in range(0, len(values), 3)]
d = numpy.array(values)
print(d)
print(d[0][1])
