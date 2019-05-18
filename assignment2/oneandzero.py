import itertools
import re

def x_num(test):
    num = 0
    for i in test:
        if 'x' in i:
           num += 1
    print(num)
    return num

def guesslist(num):
    guess = [''.join(i) for i in (itertools.product(['.', '-'], repeat=num))]
    # print(guess)
    return guess

def morse_all(test):
    xnum = x_num(test)
    guess = guesslist(xnum)
    all = []
    for replace in guess:
        possible = []
        i = 0
        for each in test:
            if 'x' in each:
                possible.append(re.sub('x', replace[i], each))
                i += 1
            else:
                possible.append(each)
        all.append(possible)
    print(all)
    return all


if __name__ == '__main__':
    # length = x_num(['x','.','x-'])
    # guesslist(length)
    morse_all(['x','.','x-'])
    morse_all(['x','x','x..','x'])
