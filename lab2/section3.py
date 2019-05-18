def find_ans(file, col1, col2):

    min = 100000
    with open(file, 'r') as csv:
        lines = csv.readlines()
        lines = lines[1:]
        for line in lines:

            first = line.split(',')[int(col1)]
            second = line.split(',')[int(col2)]
            diff = abs(int(first) - int(second))

            if diff < min:
                min = diff
                ans = line.split(',')[0]
    print(ans)

find_ans('C:/Users/yanch/Documents/dataForCode/football.csv', 5, 6)
find_ans('C:/Users/yanch/Documents/dataForCode/weather.csv', 1, 2)
