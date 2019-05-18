from itertools import *


for i in map(lambda x,y: (x, y, x*y), range(5), range(5,10)):
    print(type(i))
    print ('{} * {} = {}'.format(*i))

for i in map(pow, range(10), repeat(2)):
    print(i)