import opener

FILENAME = "data/04dayfour"

AROUND = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def ptone(lines):
    total = 0
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            count = 0
            if cell == "@":
                for val in AROUND:
                    x_val = x + val[0]
                    y_val = y + val[1]

                    if (
                        x_val > len(lines) - 1
                        or x_val < 0
                        or y_val > len(line) - 1
                        or y_val < 0
                    ):
                        continue
                    elif lines[x_val][y_val] == "@":
                        count += 1
                if count < 4:
                    total += 1

    return total


def pttwo(lines):
    total = 0
    while True:
        removed = []
        for x, line in enumerate(lines):
            for y, cell in enumerate(line):
                count = 0
                if cell == "@":
                    for val in AROUND:
                        x_val = x + val[0]
                        y_val = y + val[1]

                        if (
                            x_val > len(lines) - 1
                            or x_val < 0
                            or y_val > len(line) - 1
                            or y_val < 0
                        ):
                            continue
                        if lines[x_val][y_val] == "@":
                            count += 1
                    if count < 4:
                        removed.append((x, y))
        for val in removed:
            lines[val[0]][val[1]] = "."

        total += len(removed)
        if len(removed) == 0:
            break

    return total


def main():
    lines = opener.opener(FILENAME, ",")
    new_lines = []
    for line in lines:
        new_lines.append(list(line[0]))
    lines = new_lines
    print(ptone(lines))
    print(pttwo(lines))


main()
