import opener
START = 50
FILENAME = "data/01dayone"

def ptone(lines):
    number = START
    password = 0
    for line in lines:
        if line[0] == "L":
            number -= int(line[1:])
            while number < 0:
                number = 100 + number
        elif line[0] == "R":
            number += int(line[1:])
            while number >= 100:
                number = number - 100
        if number == 0:
            password += 1

    return password


def pttwo(lines):
    number = START
    password = 0
    for line in lines:
        if line[0] == "L":
            if number == 0:
                password -= 1
            number -= int(line[1:])
            while number <= 0:
                password += 1
                number = 100 + number
        elif line[0] == "R":
            number += int(line[1:])
            while number >= 100:
                password += 1
                number = number - 100
        if number == 100:
            number = 0

    return password


def main():
    lines = opener.opener(FILENAME)

    print(ptone(lines))
    print(pttwo(lines))


main()