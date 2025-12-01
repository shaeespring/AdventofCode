from arrayer import arrayer


def find_guard_items(array):
    guard_pos = ()
    items = []
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == "^":
                guard_pos = (x, y)
            if array[x][y] == "#":
                items.append((x, y))
    return guard_pos, items


def turn(direction):
    if direction == "^":
        return ">"
    if direction == ">":
        return "v"
    if direction == "v":
        return "<"
    if direction == "<":
        return "^"


def check(guard_pos, items):
    for item in items:
        if guard_pos == item:
            return True

    return False


def check_edges(guard_pos, array):
    if guard_pos[0] == len(array):
        return True
    if guard_pos[0] == -1:
        return True
    if guard_pos[1] == len(array[0]):
        return True
    if guard_pos[1] == -1:
        return True
    else:
        return False


def pt1_build(grid, original, items):
    s = set()
    guard_pos = original
    direction = grid[original[0]][original[1]]

    while True:
        if guard_pos != original:
            s.add(guard_pos)
        if direction == "^":
            try_guard_pos = (guard_pos[0] - 1, guard_pos[1])
        elif direction == "v":
            try_guard_pos = (guard_pos[0] + 1, guard_pos[1])
        elif direction == "<":
            try_guard_pos = (guard_pos[0], guard_pos[1] - 1)
        else:
            try_guard_pos = (guard_pos[0], guard_pos[1] + 1)

        if check(try_guard_pos, items):
            direction = turn(direction)
        else:
            guard_pos = try_guard_pos
        if check_edges(try_guard_pos, grid):
            s.add(try_guard_pos)
            break
    return s


def test_location(grid, pos_items, pos_guard):
    s = dict()
    direction = grid[pos_guard[0]][pos_guard[1]]
    while True:
        if pos_guard not in s:
            s[pos_guard] = [direction]
        elif direction in s[pos_guard]:
            return True
        else:
            s[pos_guard].append(direction)

        if direction == "^":
            try_guard_pos = (pos_guard[0] - 1, pos_guard[1])
        elif direction == "v":
            try_guard_pos = (pos_guard[0] + 1, pos_guard[1])
        elif direction == "<":
            try_guard_pos = (pos_guard[0], pos_guard[1] - 1)
        else:
            try_guard_pos = (pos_guard[0], pos_guard[1] + 1)

        if check(try_guard_pos, pos_items):
            direction = turn(direction)
        else:
            pos_guard = try_guard_pos
        if check_edges(try_guard_pos, grid):

            return False


def main():
    grid = arrayer("inputfile.txt", "")
    pos_guard, items = find_guard_items(grid)
    pt2 = 0
    seta = pt1_build(grid, pos_guard, items)
    pt1 = len(seta)
    print(pt1)

    for location in seta:
        orig_items = items[:]
        orig_items.append(location)
        if test_location(grid, orig_items, pos_guard):
            pt2 += 1

    print(pt2)

main()
