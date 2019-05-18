
min = 10000
n = 1
a = input('enter the number of first col, begin with 0')
b = input('and the second col')

n=0
min = 100000
ans = ''
with open('C:/Users/yanch/Documents/dataForCode/football.csv', 'r') as csv:
    for line in csv:
        # print(line)
        # team = line.split(',')[0]
        # print(team)
        if n == 0:
            n = n+1
            continue

        goalsfor = line.split(',')[int(a)]
        print(goalsfor)
        goalsagainst = line.split(',')[int(b)]
        diff = abs(int(goalsfor) - int(goalsagainst))
        print(diff)
        if diff < min:
            min = diff
            ans = line.split(',')[0]
    print(ans)