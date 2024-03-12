# D. Слоны и ладьи

def rook(board, i, j):
    for y in range(i - 1, -1, -1):
        if board[y][j] in 'BR':
            break
        board[y][j] = '+'

    for y in range(i + 1, 8):
        if board[y][j] in 'BR':
            break
        board[y][j] = '+'

    for x in range(j - 1, -1, -1):
        if board[i][x] in 'BR':
            break
        board[i][x] = '+'

    for x in range(j + 1, 8):
        if board[i][x] in 'BR':
            break
        board[i][x] = '+'


def bishop(board, i, j):
    for y in range(i - 1, -1, -1):
        x = y + (j - i)
        if x < 0 or board[y][x] in 'BR':
            break
        board[y][x] = '+'

    for y in range(i + 1, 8):
        x = y + (j - i)
        if x == 8 or board[y][x] in 'BR':
            break
        board[y][x] = '+'

    for y in range(i - 1, -1, -1):
        x = (i + j) - y
        if x == 8 or board[y][x] in 'BR':
            break
        board[y][x] = '+'

    for y in range(i + 1, 8):
        x = (i + j) - y
        if x < 0 or board[y][x] in 'BR':
            break
        board[y][x] = '+'


board = []
for _ in range(8):
    board.append(list(input()))

for i in range(8):
    for j in range(8):
        if board[i][j] == 'B':
            bishop(board, i, j)
        elif board[i][j] == 'R':
            rook(board, i, j)

answer = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            answer += 1

print(answer)
