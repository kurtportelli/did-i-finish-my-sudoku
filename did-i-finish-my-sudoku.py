def done_or_not(board): #board[i][j]
    for row in board:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 'Try again!'
    for j in range(9):
        column = []
        for row in board:
            column.append(row[j])
        if sorted(column) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 'Try again!'
    for i in range(3):
        for j in range(3):
            region = []
            for row in board[i*3:(i+1)*3]:
                region.extend(row[j*3:(j+1)*3])
            if sorted(region) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return 'Try again!'
    return 'Finished!'
