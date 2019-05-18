for i in range(0,50):
    if i%2 == 0:
        continue
    for n in range(3,i):
        if i%n == 0:
            break
    else:
        print (i,'is a prime number')