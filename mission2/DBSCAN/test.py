# -*- coding: utf-8 -*-

a = set()
a.add(1)
a.add(2)


b = set()
b.add(3)
b.add(4)
b.add(1)

a = a | b

for p in a:
    print p