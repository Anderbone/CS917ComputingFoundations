mylist = []
sum = 0
while(True):
    n = input()
    mylist.append(int(n))
    if n == 'stop':
        break

mylist.pop()

for i in range(0, len(mylist)):
    sum += int(mylist[i])

mylist.sort()
print(mylist)
print(str(sum/len(mylist)))