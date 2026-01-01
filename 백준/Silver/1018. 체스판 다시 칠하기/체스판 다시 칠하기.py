m, n = map(int, input().split())

matrix = [list(input()) for _ in range(m)]
board = []

for i in range(m-7):
    for j in range(n-7):
        cnt_w = 0 
        cnt_b = 0 
    
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0:
                    if matrix[row][col] != 'W': cnt_w += 1
                    if matrix[row][col] != 'B': cnt_b += 1
                else:
                    if matrix[row][col] != 'B': cnt_w += 1
                    if matrix[row][col] != 'W': cnt_b += 1

        board.append(cnt_w)
        board.append(cnt_b)

print(min(board))

    


            
