''' Module fib.py '''
#from __future__ import print_function

def even_fib(n):
    total = 0
    f1, f2 = 1, 2
    while f1 < n:
        if f1 % 2 == 0:
            total = total + f1
        f1, f2 = f2, f1 + f2
    return total
__name__ = 'notmain'
# if __name__ == "__main__":
print(__name__)
limit = input("Max Fibonaccinumber: ")
print(even_fib(int(limit)))
