from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['x', 'y', 'r'])

p = Point(1, 2)
circle = Circle(1, 2, 3)
print(p)
print(circle)

q1 = deque()
q1.append('a')
q1.appendleft('b')
print(q1)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

od = OrderedDict()
od['x'] = 'kx'
od['y'] = 'ky'
print(od)

counter = Counter()
for ch in 'programming':
    counter[ch] = counter[ch] + 1
print(counter)
