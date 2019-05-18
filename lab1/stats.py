print('please enter number, enter \'stop\' to exit')
myList = []
mySum = 0
while True:
    myInput = input()
    if myInput == 'stop':
        break
    if myInput.isdigit():
        myList.append(int(myInput))
        mySum += int(myInput)

myList.sort()
print('you entered ' + str(len(myList)) + ' numbers.')
print('Min number: ' + str(myList[0]))
print('Max number: ' + str(myList[-1]))
print('Mean: ' + str(mySum / len(myList)))
