
from itertools import permutations
import string

def find_perm(num):
    for i, p in enumerate(permutations(string.digits), start=1):
        if i == num:
            print(type(p))
            return ''.join(p)



if __name__ == "__main__":
    print ("The one millionth permutation is ", find_perm(1000000))
    print(string.digits)
