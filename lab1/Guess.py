import random
print('choose the difficulty:')
print('1 for easy')
print('2 for medium')
print('3 for hard')
dif = int(input())
ran = 0
if dif == 1:
    ran = 10
elif dif == 2:
    ran = 50
elif dif == 3:
    ran = 100

ans=random.randint(1, ran)
while(True):
    guess=input('give a number between 1 to '+str(ran)+'\n')
    g=int(guess)
    if(ans==g):
        print("you are right, the number is "+str(ans))
        break
    elif(ans<g):
        print("try something smaller")
        continue
    elif(ans>g):
        print("try something biger")
        continue

