def arrayer(filename,delimiter=" "):
    with open(filename) as file:
        array = []
        for line in file:
            if delimiter == "":
                line = line.strip()
                list(line)
            else:
                line = line.strip().split(delimiter)
            inner = []
            for c in line:
                inner.append(c)
            array.append(inner)
    return array
