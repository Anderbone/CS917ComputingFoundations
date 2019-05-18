import re


text = 'banana'
mylist = list(text)
mylist[0] = 'z'
print(mylist)
guess = 'c'
lent = len(text)
print("-" * lent)



list = []
for i in re.finditer(guess, text):
    list.append(i.start())
print(list)

def process_guess(self, guess):
    # your code here (this should be called from play)
    for i in range(0, len(self.hidden_word)):
        if self.hidden_word[i] != guess:
            print('-', end='')
        else:
            print(guess, end='')

# for i in range(0, lent):
#     if text[i] != 'a':
#         print('-', end = '')
#     else:
#         print('a', end = '')

