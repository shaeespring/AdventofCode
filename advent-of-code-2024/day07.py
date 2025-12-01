def ops_choices(line, value, ind, current_val, pt2):
    
    if ind == len(line):
        return current_val == value

    if pt2:
        val = str(current_val) + str(line[ind])
        if ops_choices(line, value, ind + 1, int(val), pt2):
            return True

    val = int(line[ind]) + current_val
    if ops_choices(line, value, ind + 1, val, pt2):
        return True

    val = int(line[ind]) * current_val
    if ops_choices(line, value, ind + 1, val, pt2):
        return True


def main():
    pt1 = 0
    pt2 = 0
    with open("inputfile.txt") as file:
        for line in file:
            line = line.strip().split()
            value = line[0]
            value = int(value[: len(value) - 1])
            check = line[1:]
            if ops_choices(check, value, 1, int(check[0]), False):
                pt1 += value
            if ops_choices(check, value, 1, int(check[0]), True):
                pt2 += value

        print(pt1)
        print(pt2)


main()
