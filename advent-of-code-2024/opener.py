def opener(filename, delimiter=None):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)

    if len(lines) == 1:
            return line
    else:
        return lines
