import opener

START = 50
FILENAME = "data/03daythree"


def ptone(lines):
    total = 0
    for line in lines:
        joltage = 0
        for i in line:
            for j in range(line.index(i) + 1, len(line)):
                string = i + line[j]
                if int(string) > joltage:
                    joltage = int(string)
        total += joltage
    return total


def pttwo(lines):
    """This is a really garbage way to do this. I had a minor crashout working on it, and this is the result of that"""
    total = 0
    joltage = 0
    for line in lines:
        digits = list(line)
        final = []
        start = 0
        for i in range(12):
            max_digit = "0"
            max_pos = start
            for j in range(start, len(digits) - (12 - i) + 1):
    
                if digits[j] > max_digit:
                    max_digit = digits[j]
                    max_pos = j
                    if max_digit == "9":
                        break

            final.append(max_digit)
            start = max_pos + 1

        joltage = int("".join(final))
        total += joltage

    return total


def main():
    lines = opener.opener(FILENAME)

    print(ptone(lines))
    print(pttwo(lines))


main()
