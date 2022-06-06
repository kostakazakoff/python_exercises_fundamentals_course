l1 = list(map(int, filter(lambda x: x != ' ', input())))
l2 = list(map(int, filter(lambda x: x != ' ', input())))
l3 = list(map(int, filter(lambda x: x != ' ', input())))


def tic_tac_toe(row_1, row_2, row_3):
    gamepad = [row_1, row_2, row_3]
    result = ''
    for _ in range(2):
        diagonal = []
        for i in range(3):
            row = gamepad[i]
            column = [row_1[i], row_2[i], row_3[i]]
            diagonal += [gamepad[i][i]]
            if row.count(1) == 3 or column.count(1) == 3 or diagonal.count(1) == 3:
                result = 'First player won'
            elif row.count(2) == 3 or column.count(2) == 3 or diagonal.count(2) == 3:
                result = 'Second player won'
        gamepad.reverse()
    if result == '':
        result = 'Draw!'
    return result


print(tic_tac_toe(l1, l2, l3))
