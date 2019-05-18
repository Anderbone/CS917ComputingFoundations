class Team:
    def __init__(self, name='', goalsfor=0, goalsagainst=0):
        self.name = name
        # print('myteam name is '+ name)
        self.goalsfor = goalsfor
        self.goalsagainst = goalsagainst
        self.diff = abs(int(goalsfor) - int(goalsagainst))
min = 10000
n = 1
with open('C:/Users/yanch/Documents/dataForCode/football.csv', 'r') as csv:
    for line in csv:
        # print(line)
        team = line.split(',')[0]
        # print(team)
        if team == 'Team':
            continue
        goalsfor = line.split(',')[5]
        goalsagainst = line.split(',')[6]
        locals()['team'+str(n)] = Team(team, goalsfor, goalsagainst)
        if locals()['team'+str(n)].diff<min:
            min = locals()['team'+str(n)].diff
            ans = locals()['team'+str(n)].name
        n = n+1
print(ans)