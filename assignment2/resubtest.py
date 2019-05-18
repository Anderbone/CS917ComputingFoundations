import re

ans = re.sub('a','bb','sfaasda')
print(ans)

b= set()
b.add((1,0))
b.add((1,1))
x = (1,0)
b.remove(x)
# b.remove((1,0))
print(type(b))
print(b)

for each in b:
    print(each)
    print(each[0])

my1 = [(5, 7), (5, 6), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2), (2, 2), (1, 2), (1, 1), (1, 0)]
print(my1)
my1.reverse()
print(my1)



