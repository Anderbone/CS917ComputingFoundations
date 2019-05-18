while True:
    try:
        x = input('enter a number')
        if x =='stop':
            break
        x = int(x)
    except ValueError:
        print('oops! not a number')

