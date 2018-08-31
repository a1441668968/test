from collections import namedtuple

p1 = (10, 20)
print(p1[0])
test = namedtuple('test', ['x', 'y', 'z'])
p2 = test(1, 2, 3)
print(p2[0])
print(p2.x)
