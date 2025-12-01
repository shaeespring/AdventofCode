def opener(filename):
    with open(filename) as file:
        return [line.strip().split() for line in file]

def check_line(line):
    valid = True  # if the line is valid
    diff = int(line[1]) - int(line[0])
    # dec
    if diff < 0:
        for num in range(1, len(line)):
            diff = int(line[num]) - int(line[num - 1])
            if diff > -1 or diff < -3:
                valid = False

    # inc
    elif diff > 0:
        for num in range(1, len(line)):
            diff = int(line[num]) - int(line[num - 1])
            if diff < 1 or diff > 3:
                valid = False
    else:
        valid = False
    return valid


def main():
    lines = opener("inputfile.txt")
    pt1 = sum(check_line(line) for line in lines)
    print(pt1)
    pt2 = 0
    for line in lines:
        if check_line(line):
            pt2 += 1
        else:
            for num in range(len(line)):
                # copy of line
                moddedline = line[:]
                moddedline.pop(num)
                if check_line(moddedline):
                    pt2 += 1
                    break
    print(pt2)


main()
