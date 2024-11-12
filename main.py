# Игра крестики нолики
def check_winner():
    if area [0][0] == 'X' and area [0][1] == 'X' and area [0][2] == 'X':
        return "X"
    if area  [1][0] == 'X' and area [1][1] == 'X' and area [1][2] == 'X':
        return "X"
    if area  [2][0] == 'X' and area [2][1] == 'X' and area [2][2] == 'X':
        return "X"

    if area  [0][0] == 'X' and area [1][0] == 'X' and area [2][0] == 'X':
        return "X"
    if area  [0][1] == 'X' and area [1][1] == 'X' and area [2][1] == 'X':
        return "X"
    if area  [0][2] == 'X' and area [1][2] == 'X' and area [2][2] == 'X':
        return "X"

    if area  [0][0] == 'X' and area [1][1] == 'X' and area [2][2] == 'X':
        return "X"
    if area  [0][2] == 'X' and area [1][1] == 'X' and area [2][0] == 'X':
        return "X"

    if area [0][0] == 'O' and area [0][1] == 'O' and area [0][2] == 'O':
        return 'O'
    if area [1][0] == 'O' and area [1][1] == 'O' and area [1][2] == 'O':
        return 'O'
    if area [2][0] == 'O' and area [2][1] == 'O' and area [2][2] == 'O':
        return 'O'

    if area [0][0] == 'O' and area [1][0] == 'O' and area [2][0] == 'O':
        return 'O'
    if area [0][1] == 'O' and area [1][1] == 'O' and area [2][1] == 'O':
        return'O'
    if area [0][2] == 'O' and area [1][2] == 'O' and area [2][2] == 'O':
        return 'O'

    if area [0][0] == 'O' and area [1][1] == 'O' and area [2][2] == 'O':
        return 'O'
    if area [0][2] == 'O' and area [1][1] == 'O' and area [2][0] == 'O':
        return 'O'

    return '*'


def draw_area():
    for i in area:
        print(*i)
    print()

area =[['*','*','*'] , ['*','*','*'] , ['*','*','*']]
print('Давайте сыграем в крестики нолики:')
print('----------------------------------')
draw_area()
for turn in range (1 , 10):
    print(f'Ход : {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ход второго игрока")
    else:
        turn_char = 'Х'
        print("Ход первого игрока")

    row = int (input('Введите номер по горизонтале (1 ,2,3,): ')) -1
    column = int (input('Введите номер по вертикале (1 ,2,3,): ')) -1
    if  area [row] [column] =='*':
        area [row] [column] = turn_char
    else:
        print('Ячейка занята , Вы пропускаете ход! ')
        draw_area()
        continue

    draw_area()

    if check_winner()  == 'X':
        print('Победа Первого Игрока: ')
        break

    if check_winner()  == 'O':
        print('Победа Второго Игрока: ')
        break

    if check_winner() == '*'  and turn == 9:
        print('НИЧЬЯ:)')
        break

