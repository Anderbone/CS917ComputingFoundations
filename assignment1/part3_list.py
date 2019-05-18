height = 5
width = 10
board = [['-']*width for i in range(height)]
board[1][1] = 'b'
board[2][1] = 'a'
board[3][1] = 'g'
board[1][2] = 'a'
board[1][3] = 'd'
board[0][3] = 'z'
board[0][8] = 'p'
board[0][9] = 'z'

for i in board:
    print(''.join(i))

x = 0
while x < height:
    y = 0
    while y < width:
        if board[x][y] != '-' and y+1 < width and board[x][y+1] != '-':
            i = 1
            word = [board[x][y]]
            while y+i < width and board[x][y+i] != '-':
                word.append(board[x][y+i])
                i += 1
            y = y + i
            print(word)
        y += 1
    x += 1


# y = 0
# while y < width:
#     x = 0
#     while x < height:
#         if board[x][y] != '-' and x + 1 < height and board[x + 1][y] != '-':
#             i = 1
#             word = [board[x][y]]
#             while (x + i < height and board[x + i][y]) != '-':
#                 word.append(board[x + i][y])
#                 i += 1
#             x = x + i
#             print(word)
#         x += 1
#     y += 1
#


