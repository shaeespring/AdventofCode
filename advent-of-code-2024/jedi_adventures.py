import random

# GLOBALS
ROWS = 3
COLUMNS = 9

VADER = "V"
MAUL = "M"
SITHS = [VADER, MAUL]

KYBER_CRYSTAL = "K"
LENS = "L"
POWER = "P"
HILT = "H"
LIGHTS = [HILT, KYBER_CRYSTAL, LENS, POWER]


NV = chr(9608)
LOC = (NV, False)
JEDI = "J"
UP = "u"
DOWN = "d"
LEFT = "l"
RIGHT = "r"
MOVE = [UP, DOWN, LEFT, RIGHT]


def make_table(rows, cols):
    # return 2d list
    # table=[]
    return [[(NV, False) for _ in range(cols)] for _ in range(rows)]


def find_empty_position(board):
    while True:
        x = random.randrange(0, ROWS)
        y = random.randrange(0, COLUMNS)

        pos = (x, y)

        # Check the value at the selected position
        if board[x][y] == (NV, False):
            return pos


def place_pieces(board):
    for item in SITHS:
        (x, y) = find_empty_position(board)
        board[x][y] = (item, False)

    for item in LIGHTS:
        (x, y) = find_empty_position(board)
        board[x][y] = (item, False)
    for item in JEDI:
        (x, y) = find_empty_position(board)

        new_item = board[x][y][0]
        if new_item == NV:
            board[x][y] = (" ", True)
        else:
            board[x][y] = (new_item, True)

        loc_jedi = (x, y)

    return (board, loc_jedi)


def is_sith(item):
    for sith in SITHS:
        if item == sith:
            return True
    return False


def is_light(item):
    for light in LIGHTS:
        if item == light:
            return True
    return False

def is_not_in_list(item,list):
    for i in list:
        if item == i:
            return False
    return True

def display(board, jedi_pos, num_moves, col_list, sla_list):
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            item = row[j]
            # Display the Jedi character if True, else NV
            if (i, j) == jedi_pos:
                print(JEDI, end="")
            elif item[1] == True:  # Check the second element (True or False)
                print(item[0], end="")
            else:
                print(NV, end="")  # Display empty space
        print()  # New line after each row

    print("Collected Lightsaber Parts", len(col_list), "/ 4:", col_list)
    print("Slain Sith Lords", len(sla_list), "/ 2: ", sla_list)
    print_jedi = (jedi_pos[0] + 1, jedi_pos[1] + 1)
    print("Position:", print_jedi, "\t\t", "Moves:", num_moves)


def move(board, jedi_pos, dir):
    try:
        if dir == UP:
            try_jedi_pos = (jedi_pos[0] - 1, jedi_pos[1])
        elif dir == DOWN:
            try_jedi_pos = (jedi_pos[0] + 1, jedi_pos[1])
        elif dir == LEFT:
            try_jedi_pos = (jedi_pos[0], jedi_pos[1] - 1)
        elif dir == RIGHT:
            try_jedi_pos = (jedi_pos[0], jedi_pos[1] + 1)
        else:
            raise ValueError

        if try_jedi_pos[0] > len(range(ROWS)) - 1 or try_jedi_pos[0] < 0:
            raise ValueError
        if try_jedi_pos[1] > len(range(COLUMNS)) - 1 or try_jedi_pos[1] < 0:
            raise ValueError

        item = board[try_jedi_pos[0]][try_jedi_pos[1]]

        new_item = item[0]
        if new_item == NV:
            new_item = " "
        board[try_jedi_pos[0]][try_jedi_pos[1]] = (new_item, True)  # Set new position
        return (board, try_jedi_pos, item)

    except ValueError:
        print("Invalid Move!")
        return (board, jedi_pos, None)


def main():
    num_moves = 0
    col_list = []
    sla_list = []
    print("Sith Lords:", SITHS)
    print("Lightsaber Parts:", LIGHTS)
    print("May the Force Be With You!")
    board = make_table(ROWS, COLUMNS)
    board, jedi_pos = place_pieces(board)
    display(board, jedi_pos, num_moves, col_list, sla_list)
    while True:
        dir = input(">")
        if dir == "q":
            break

        else:
            board, jedi_pos, item = move(
                board, jedi_pos, dir
            )
            if item != None:
                num_moves += 1
                if is_sith(item[0]): #if item[0] in SITH
                    if len(col_list) == 4:
                        if is_not_in_list(item[0],sla_list):
                            print("You have slain a Sith Lord:", item[0])
                            sla_list.append(item[0])
                    else:
                        print(
                            "You've found a Sith without a lightsaber and have been slain"
                        )
                        print("Goodbye!")
                        exit()
                elif is_light(item[0]):
                    if is_not_in_list(item[0],col_list):
                        print("You collected a lightsaber part:", item[0])
                        col_list.append(item[0])
            display(board, jedi_pos, num_moves, col_list, sla_list)


if __name__ == "__main__":
    main()
