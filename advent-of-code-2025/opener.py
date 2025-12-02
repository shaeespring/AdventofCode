def opener(filename, delimiter=None):
    """Opens @param filename and splits each line on @param delimiter to parse into an array"""
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if delimiter is not None:
                line = line.split(delimiter)
            lines.append(line)

    if len(lines) == 1:
            return line
    else:
        return lines
    file.close()
