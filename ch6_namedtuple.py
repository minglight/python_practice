from collections import namedtuple

Duck = namedtuple('Duck2', 'bill tail')

if __name__ == '__main__':
    duck1 = Duck("orange", "long")
    print(duck1.bill)
    print(duck1.tail)

    options = {'bill': 'pink', "tail":"short"}
    duck2 = Duck(**options)
    print(duck2.bill)
    print(duck2.tail)


dic = {'a':1, 'b':2}
for k in dic:
    print(k)


s = set()
s.add('b')
s.add('c')
print(s)