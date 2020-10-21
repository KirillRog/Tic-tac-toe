def tic_tac_toe():
    gl = list(9 * ' ')
    grid = '''
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
    '''.format(*gl)
    print(grid)
    while True:
        xo = choose_symbol(gl)
        gl = turn(gl, xo)
        grid = '''
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
    '''.format(*gl)
        print(grid)
        tr, mr, br, lc, mc, rc, ld, rd = gl[:3], gl[3:6], gl[6:], gl[::3], gl[1::3], gl[2::3], gl[::4], gl[2:8:2]
        combinations = [tr, mr, br, lc, mc, rc, ld, rd]
        row_win = [x[0] if len(set(x)) == 1 else None for x in combinations]
        outcome = set([x for x in row_win if x is not None])
        if  'X' in outcome or 'O' in outcome:
            result = str(list(outcome)[0] + " wins")
            break
        if gl.count(" ") == 0:
            result = "Draw"
            break
    return result


def turn(grid_list, symbol):
    coords = input('Enter the coordinates:')
    if coords.isalpha():
        print("You should enter numbers!")
        return turn(grid_list, symbol)
    else:
        num_turn = [int(i) for i in coords.split(' ')]
        for i in num_turn:
            if i not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
                return turn(grid_list, symbol)
        if grid_list[(num_turn[0] - 1) + ((3 - num_turn[1]) * 3)] == ' ':
            grid_list[(num_turn[0] - 1) + ((3 - num_turn[1]) * 3)] = symbol
            return grid_list
        else:
            print('This cell is occupied! Choose another one!')
            return turn(grid_list, symbol)


def choose_symbol(grid_list):
    return 'X' if grid_list.count('X') == grid_list.count('O') else 'O'


print(tic_tac_toe())
